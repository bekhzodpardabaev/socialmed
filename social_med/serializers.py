from rest_framework import serializers
from .models import News, Ads, Categories


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
