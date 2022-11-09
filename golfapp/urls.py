from django.urls import path
from .views import ClubListView, ClubDetailView, ClubCreateView, ClubUpdateView, ClubTListView
from . import views

urlpatterns = [
    path('clublist/', ClubListView.as_view(), name='c_list'),
    path('<int:pk>/', ClubDetailView.as_view(), name='c_detail'),
    path('new/', ClubCreateView.as_view(), name='c_new'),
    path('<int:pk>/edit/', ClubUpdateView.as_view(), name='c_edit'),
    path('ctlist/', ClubTListView.as_view(), name='ct_list'),
]