from rest_framework import serializers
from .models import *


class DigitalProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:editdigitalprofile-detail")  # CALL JOB DETAIL ROUTER

    class Meta:
        model = DigitalProfile
        fields = ['url', 'id', 'user', 'company_name', 'company_logo']


class DigitalProfileMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = DigitalProfile
        fields = ['id']


class EditDigitalProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    company_name = serializers.ReadOnlyField()
    approved = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = '__all__'


class PersonalDetailSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditpersonaldetail-detail")

    class Meta:
        model = PersonalDetail
        fields = '__all__'


class SocialMediaLinksSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditsocialmedialinks-detail")

    class Meta:
        model = SocialMediaLinks
        fields = '__all__'


class PaymentDetailSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditpaymentdetail-detail")

    class Meta:
        model = PaymentDetail
        fields = '__all__'


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditservices-detail")

    class Meta:
        model = Services
        fields = '__all__'


class EcommerceSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditecommerce-detail")

    class Meta:
        model = Ecommerce
        fields = '__all__'


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditgallery-detail")

    class Meta:
        model = Gallery
        fields = '__all__'


class ApproveDigitalProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:approvedigitalprofiledetail-detail")
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = '__all__'


class ApproveDigitalProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = ['user', 'company_name', 'date', 'approved']
