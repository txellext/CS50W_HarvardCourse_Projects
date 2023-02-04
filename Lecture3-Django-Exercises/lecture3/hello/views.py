from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse

# Create your views here.

# Create index function that return HttpResponse
def index(request):
    return HttpResponse("Hello, world!")