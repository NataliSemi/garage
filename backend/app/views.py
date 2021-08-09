from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User, AnonymousUser
# Create your views here.
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication




class LoginAPIView(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request, format=None):
        if not isinstance(request.user, AnonymousUser):
            content = {
                'id': request.user.id,
                'user': UserSerializer(request.user).data,  # `django.contrib.auth.User` instance.
            }
            return Response(content)
        else:
            return Response({"error": "not logged in"}, 401)

    def post(self, request):
        user = authenticate(request,
                                                username=request.data['username'],
                                                password=request.data['password'])
        if user:
            login(request, user)
            token = Token.objects.get_or_create(user=request.user)[0].key
            return Response(headers={'Authorization': f'Token {token}'})
        else:
            return Response({"error": "not valid credentials"}, 401)

            