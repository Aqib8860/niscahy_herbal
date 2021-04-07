from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsOwner
from core.models import User
from core.permissions import SubscribedUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class DigitalProfileViewSet(viewsets.ModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = DigitalProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
