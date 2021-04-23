from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets
from api.permission import IsOwner


class UserView(viewsets.ModelViewSet):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
