from django.urls import path
from . import views

app_name = "tasks" # We define an app name in order to not get confused about path names: tasks:index, tasks:add
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]