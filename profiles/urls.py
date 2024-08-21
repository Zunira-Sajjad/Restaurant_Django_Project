from .views import ProfileDetailView
from django.urls import path

urlpatterns = [
    path('<str:username>/', ProfileDetailView.as_view() , name='detail'),
]