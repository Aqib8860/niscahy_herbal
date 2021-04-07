from django.urls import path, include
from digitalprofile import views
from rest_framework import routers


app_name = 'digitalprofile'

router = routers.DefaultRouter()
router.register('view-add-digital-profile', views.DigitalProfileViewSet, basename='viewadddigitalprofile')


urlpatterns = [
    path('', include(router.urls)),
]
