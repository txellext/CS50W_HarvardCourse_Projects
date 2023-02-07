from django import forms 
from django.shortcuts import render

tasks = ["resume", "letter", "logo" ]
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") # Name of the new task
    priority = forms.IntegerField(label = "Priority", min_value=1, max_value=10) 
     

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })