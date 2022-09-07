from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Ads, Categories
from .serializers import NewsSerializer, AdsSerializer, CategorySerializer


class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdateView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'


class AdsCreateView(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class NewsDetailView(APIView):
    def get(self, request, id):
        news = News.objects.get(id=id)
        news.views += 1
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class AdsDetailView(APIView):
    def get(self, request, id):
        ads = Ads.objects.get(id=id)
        serializer = AdsSerializer(ads)
        return Response(serializer.data)


class AdsUpdateView(generics.UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = 'id'
