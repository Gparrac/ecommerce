from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView
class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectamente'
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self, request, *arg, **kwargs):
        # it's already done in super() however we can rewrite it to make it more clear or get a different way
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            print(login_serializer.validated_data['user'])
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                print('is actived', created)
                user_serializer = UserTokenSerializer(user)
                if created: 
                    print('is actived')
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso!'
                    }, status = status.HTTP_201_CREATED)
                else:
                    # get and delete all sessions to avoid two users with session actived at the same time
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({'token': token.key, 'user': user_serializer.data, 'message': 'Inicio de sesión Exitoso'}, status = status.HTTP_201_CREATED)
                    
            else:
                return Response({'error': 'Este usuarion no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else: 
            return Response({'message': 'Credenciales incorrectas '}, status=status.HTTP_400_BAD_REQUEST)
        
class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:         
            token = Token.objects.filter(key = request.GET.get('token', '')).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'            
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en petición'}, status = status.HTTP_409_CONFLICT)