from django.urls import path
from .views import NewsDetailView, NewsCreateView, NewsUpdateView, AdsCreateView, AdsListView, NewsListView, \
    AdsDetailView, AdsUpdateView, OrganizationListView, OrganizationDetailView, ServiceListView, ServiceDetailView, \
    ApplyCreateView, DashboardDetailView, DashboardView

urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('news/<int:id>/', NewsDetailView.as_view()),
    path('news/create/', NewsCreateView.as_view()),
    path('news/update/<int:id>/', NewsUpdateView.as_view()),
    path('ads/create/', AdsCreateView.as_view()),
    path('ads/', AdsListView.as_view()),
    path('ads/<int:id>/', AdsDetailView.as_view()),
    path('ads/update/<int:id>/', AdsUpdateView.as_view()),
    path('organization/', OrganizationListView.as_view()),
    path('organization/<int:id>/', OrganizationDetailView.as_view()),
    path('service/', ServiceListView.as_view()),
    path('service/<int:id>/', ServiceDetailView.as_view()),
    path('apply/', ApplyCreateView.as_view()),
    path('dashboard/detail/<int:pk>/', DashboardDetailView.as_view()),
    path('dashboard/', DashboardView.as_view())
]
