from django.shortcuts import render

tasks = ["resume", "letter", "logo" ]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })