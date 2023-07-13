# views.py
from django.contrib.auth.models import User, Group, Permission
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from apps.auths.serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
