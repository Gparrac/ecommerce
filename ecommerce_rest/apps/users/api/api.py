from rest_framework.views import APIView
from apps.users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer, UserListSerializer, TestUserSerializer

# class UserApiView(APIView):
    # def get(self, request):
    #     users = User.objects.all()
    #     users_serializer = UserSerializer(users, many = True)
    #     return Response(users_serializer.data)
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id','username','email', 'password')
        users_serializer = UserListSerializer(users, many = True)
        # test_data = {
        #     'name': 'test',
        #     'email': 'develop@gmail.com'
        # }
        # test_user = TestUserSerializer(data = test_data, context = test_data)
        # if test_user.is_valid():
        #     print("Paso validaciones")
        #     test_user.save()
        # else:
        #     print(test_user.errors)
        return Response(users_serializer.data)
        
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)
@api_view(['GET','PUT'])
def user_detail_api_view(request,pk=None):
    if request.method == 'GET':
            print('passing')
            user = User.objects.filter(id = pk).first()
            user_serializer = UserSerializer(user)
            print('passingWWEWEW')
            return Response(user_serializer.data)
    elif request.method == 'PUT':
        
        user = User.objects.filter(id = pk).first()
        print('passing update?', request.data)
        user_serializer = UserSerializer(user, data = request.data, context = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)