from django.shortcuts import render
from django.contrib.auth.models import Group
from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics,mixins
from django.contrib.auth import authenticate
from datetime import datetime
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from  rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.hashers import make_password,check_password



@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request=request, email=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        response = UserSerializer(user).data
        response['token'] = token.key
        return Response(response, status=200)
    return Response({"detail": "Invalid credentials"}, status=400)



@api_view(['POST'])
def user_register(request):
   
    name = request.data['name']
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    check_user = User.objects.filter(email=email).first()
    if check_user:
        return Response({"detail": "A user with this email is already exist. "}, status=403)


    if phone_number:
        if not str(phone_number).startswith('+250'):
            return Response({"detail": "Phone number must start with '+250'. "}, status=404)

        if not len(str(phone_number).strip()) == 13:
            return Response({"detail": "Phone number must be a rwandan number."}, status=404)

    if name and email and phone_number and password:
        user = User(
            name=name,
            email=email,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()

        response = {
            "user":UserSerializer(user).data,
            "message":"User created successful. "
        }

        return Response(response, status=200)

    return Response({"detail": "Bad request."}, status=400)



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def change_password(request, format=None):
    """
    old_password -- Oldpass
    new_password -- newpass
    """ 
    old_password = request.data['old_password']
    new_password = request.data.get('new_password')

    user = request.user

    if user:
        if check_password(old_password, user.password):
            user.set_password(new_password)
            user.save()

            return Response({"res": "Password has been changed successfully. "}, status=200)

        return Response({"detail": "Old password is incorrect"}, status=400)

    return Response({"detail": "User not found."}, status=404)
    

class UserList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs) 

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class UserDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
        

    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)

