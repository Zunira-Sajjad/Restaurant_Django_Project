from django.urls import path
from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView,
    ItemListView,
)

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='menus-create'),
    path('<int:pk>/', ItemUpdateView.as_view(), name='menus-detail'),  # Corrected path
    #path('<int:pk>/edit/', ItemUpdateView.as_view(), name='menus-edit'),  # Update view path
    path('', ItemListView.as_view(), name='menus'),  # List view path
]
