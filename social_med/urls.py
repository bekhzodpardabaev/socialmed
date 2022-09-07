from django.urls import path
from .views import NewsDetailView, NewsCreateView, NewsUpdateView, AdsCreateView, AdsListView, NewsListView, \
    AdsDetailView, AdsUpdateView

urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('news/<int:id>/', NewsDetailView.as_view()),
    path('news/create/', NewsCreateView.as_view()),
    path('news/update/<int:id>/', NewsUpdateView.as_view()),
    path('ads/create/', AdsCreateView.as_view()),
    path('ads/', AdsListView.as_view()),
    path('ads/<int:id>/', AdsDetailView.as_view()),
    path('ads/update/<int:id>/', AdsUpdateView.as_view())
]