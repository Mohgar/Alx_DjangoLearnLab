from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, UserSerializers
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)  # Get or create token
        return Response({'token': token.key})

class UserView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get(self, request):
        serializer = UserSerializers(request.user)  # Serialize user data
        return Response(serializer.data)
