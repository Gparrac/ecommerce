from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
import traceback
class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    def expires_in(self, token):
        time_elaped = timezone.now() - token.created
        #left time
        print('timeeee', time_elaped, timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS))
        return  timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elaped
        
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            print("TOKEN EXPIRADO")
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user )
        return is_expire, token
    def authenticate_credentials(self, key):
        message, user, token = (None, None, None)
        try:
            token = self.get_model().objects.select_related('user').get(key = key)            
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido'            
        is_expired = self.token_expire_handler(token)
        if is_expired:
            message = 'Su Token ha expirado.'
            user = None
            token = None


        
        return (user, token, message, self.expired)
class Authentication(object):
    user = None
    user_token_expired = False

    def get_user(self, request):
        token = get_authorization_header(request).split()
        print(token)
        if token:
            try:
                token = token[1].decode()
                print('>>>>>>', token)
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            
            user, token, message, self.user_token_expired = token_expire.authenticate_credentials(token)            
            return {'user': user, 'token': token, 'message': message}
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        print(user)
        if user == None:
            response = Response({'error': user, 'expired': self.user_token_expired}, status=status.HTTP_401_UNAUTHORIZED)
        if type(user) == dict and user.get('token',False) != None and user.get('user', False) != None:
            return super().dispatch(request, *args, **kwargs)
        else:
            response = Response({'error': user.get('message', 'Error en autenticación')}, status= status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response