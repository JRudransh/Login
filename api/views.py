from django.contrib.auth.models import User
from api.serializers import UserSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    queryset = User.objects.all()
    parser_classes = UserSerializer
