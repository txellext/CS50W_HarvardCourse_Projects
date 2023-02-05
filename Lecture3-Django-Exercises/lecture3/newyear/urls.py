from django.urls import path
from . import views # from cd import views in order to get the function 

urlpatterns = [
    path("", views.index, name="index")
]