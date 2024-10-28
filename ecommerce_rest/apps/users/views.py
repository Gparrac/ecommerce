from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer
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
                return Response({'error': 'Este usuarion no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else: 
            return Response({'message': 'Credenciales incorrectas '}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Hola estatus code '}, status=status.HTTP_200_OK)