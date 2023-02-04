from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse

# Create your views here.

# Create index function that return HttpResponse
def index(request):
    #return HttpResponse("Hello, world!")
    return render (request, "hello/index.html") # I can runder an entire html file, we prefix our templates with the project name

def txell(request):
    return HttpResponse("Hello, Txell")


def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", { # Render an entire page with a third optional argument, context, all info to the template
        "name": name.capitalize()
    }) 