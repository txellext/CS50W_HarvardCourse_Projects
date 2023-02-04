# In order to link an URL to index function in views.py, 
# we ceate this urls.py document 

from django.urls import path
from . import views # from cd import views in order to get the index function 

urlpatterns = [
    path("", views.index, name="index"), # variables: URL name, function and reference name to the URL
    path("<str:name>",views.greet, name="greet" ), # route of any string
    path("txell", views.txell, name="txell"),

]