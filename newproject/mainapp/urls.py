from django.urls import path
from .views import Indexview
from .views import Registerview
from .views import Loginview
from .views import Logoutview

urlpatterns = [
    path('home/', Indexview, name="home"),
    path('', Registerview, name="register"), 
    path('login/', Loginview, name="login"),
    path('logout/', Logoutview, name="logout"),
]