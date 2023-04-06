from django.urls import path
from .views import StartView, AnimalListView, AnimalDetailView

urlpatterns = [
    path('', StartView.as_view(), name='start'),
    path('animals', AnimalListView.as_view(), name='animal-list'),
    path('animals/<pk>', AnimalDetailView.as_view(), name='animal-detail'),
]
