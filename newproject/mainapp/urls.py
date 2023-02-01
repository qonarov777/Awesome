from django.urls import path
from .views import Indexview
from .views import Registerview
from .views import Loginview
from .views import Logoutview

urlpatterns = [
    path('home/', Loginview, name="login"),
    path('register/', Registerview, name="register"), 
    path('', Indexview, name="home"),
    path('logout/', Logoutview, name="logout"),
]