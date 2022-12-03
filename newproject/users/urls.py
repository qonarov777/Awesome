from django.urls import path
from .views import Userview

urlpatterns = [
    path('', Userview),
]