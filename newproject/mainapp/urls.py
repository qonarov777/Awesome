from django.urls import path
from .views import Indexview

urlpatterns = [
    path('', Indexview),
]