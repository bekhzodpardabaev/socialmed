from django.db.models import F, Count, Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Ads, Categories, Organization, MedicalCategory, Services, Apply
from .serializers import NewsSerializer, AdsSerializer, CategorySerializer, OrganizationSerializer, \
    OrganizationDetailSerializer, ServiceSerializer, ServiceDetailSerializer, ApplySerializer
from django_filters import rest_framework
from rest_framework import filters


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


class OrganizationListView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('medical_category',)
    search_fields = ('name', 'address')


class OrganizationDetailView(APIView):
    def get(self, request, id):
        queryset = Organization.objects.get(id=id)
        serializer = OrganizationDetailSerializer(queryset)
        return Response(serializer.data)


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title', 'subtitle')


class ServiceDetailView(APIView):
    def get(self, request, id):
        service = Services.objects.get(id=id)
        serializer = ServiceDetailSerializer(service)
        return Response(serializer.data)


class ApplyCreateView(generics.CreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer


class DashboardDetailView(APIView):
    def get(self, request, pk):
        dg_new = Apply.objects.filter(service=pk).filter(status='NEW').extra({'date': "date(date)"}).values(
            'date').annotate(
            count=Count('id')).values_list('date', 'count')
        dg_completed = Apply.objects.filter(service=pk).filter(status='COMPLETED').extra({'date': "date(date)"}).values(
            'date').annotate(
            count=Count('id')).values_list('date', 'count')
        dg_rejected = Apply.objects.filter(service=pk).filter(status='REJECTED').extra({'date': "date(date)"}).values(
            'date').annotate(
            count=Count('id')).values_list('date', 'count')
        st_new = Apply.objects.filter(service=pk).filter(status='NEW').aggregate(count=Count('id'))
        st_completed = Apply.objects.filter(service=pk).filter(status='COMPLETED').aggregate(count=Count('id'))
        st_rejected = Apply.objects.filter(service=pk).filter(status='REJECTED').aggregate(count=Count('id'))
        return Response({
            "diagram": {
                'new': dg_new,
                'completed': dg_completed,
                'rejected': dg_rejected
            },
            "statistics": {
                'new': st_new,
                'completed': st_completed,
                'rejected': st_rejected
            }
        })


class DashboardView(APIView):
    def get(self, request):
        category = Categories.objects.all()
        length = len(category)
        categories = []
        for i in range(length):
            categories.append({f"{category[i].name}": Services.objects.prefetch_related('apply').filter(apply__status='COMPLETED').filter(category=category[i].id).count()})
        for i in range(length):
            for j in range(i+1, length):
                if sum(categories[i].values()) <= sum(categories[j].values()):
                    categories[i], categories[j] = categories[j], categories[i]
        return Response({
            "top": categories
        })
