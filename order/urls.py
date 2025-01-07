from django.urls import path
from .views  import *


urlpatterns = [
    path('start_order/',start_order,name="start_order"),
]
