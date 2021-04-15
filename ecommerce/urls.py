from django.urls import path, include
from ecommerce.views import *
from rest_framework import routers


app_name = 'ecommerce'

router = routers.DefaultRouter()

router.register('view-add-edit-product-rating-review', RatingReviewViewSet, basename='viewadddeditproduct')
router.register('view-add-edit-product', ProductViewSet, basename='viewadddeditproduct')

urlpatterns = [
    path('', include(router.urls)),
    path('product-rating-review/<int:id>', ProductRatingReviewAPI.as_view(), name='productratingreview'),
]
