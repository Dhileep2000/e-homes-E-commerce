from django.urls import path
from .views import *



urlpatterns = [
    path('',homepage,name="home"),
    path('shop/',shoppage,name="shop"),
    path('myaccount/',myaccount,name="myaccount"),
    path('myaccount/edit/',edit_myaccount,name="edit_myaccount"),
    path('signup/',signuppage,name="signup"),
    path('login/',loginpage,name="login"),
    path('logout/',logoutpage,name="logout"),
]