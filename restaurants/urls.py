from django.urls import path

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
)

urlpatterns = [
    path('create/', RestaurantCreateView.as_view(), name='restaurants-create'),
    #path('<slug:slug>/edit/', RestaurantUpdateView.as_view(), name='restaurants-edit'),  # Correct syntax for pk
    path('<slug:slug>/', RestaurantUpdateView.as_view(), name='restaurants-detail'),
    path('', RestaurantListView.as_view(), name='restaurants'),
]