from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class UserSerializerAPIViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['post', 'head','options']

	def get_permissions(self):
        if self.action == 'post':
            permission_classes = [IsAuthenticated]
            # user = self.queryset.get(id=self.request.user.id)
            # if user.isadmin:
            #     permission_classes = [IsAuthenticated]
            # else:
            #     return Response("error",status=401)
        else:
            permission_classes = [IsAdminUser]
            # permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
