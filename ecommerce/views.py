from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from core.models import User
from core.permissions import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_admin is False:
            return Response({"error": "You are not Admin"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)


class RatingReviewViewSet(viewsets.ModelViewSet):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def create(self, request, *args, **kwargs):
        # if request.user.is_admin is False:
        # return Response({"error": "You are not Admin"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)


class ProductRatingReviewAPI(generics.RetrieveAPIView):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Product Does not exist"}, status=400)

        queryset = self.queryset.filter(product=product)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
