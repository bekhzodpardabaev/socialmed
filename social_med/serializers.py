from rest_framework import serializers
from .models import News, Ads, Categories, MedicalCategory, Organization, Services, Apply


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'create_date', 'img', 'subtitle', 'text', 'views')


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('title', 'create_date', 'img', 'subtitle', 'text')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name',)


class OrganizationSerializer(serializers.ModelSerializer):
    # category = serializers.CharField()

    class Meta:
        model = Organization
        fields = ('name', 'medical_category', 'address', 'metro', 'start_time', 'end_time', 'latitude', 'longitude')


class OrganizationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'address', 'metro', 'start_time', 'end_time')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('title', 'subtitle', 'category')


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('title', 'subtitle', 'how_it_works', 'service_information', 'required_documents', 'organization',
                  'responsible_person', 'law', 'contact')


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ('service', 'text', 'status', 'date')
