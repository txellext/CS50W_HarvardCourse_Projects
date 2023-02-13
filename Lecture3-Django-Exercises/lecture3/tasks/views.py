from django import forms 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

tasks = []
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") # Name of the new task
    priority = forms.IntegerField(label = "Priority", min_value=1, max_value=10) 
     

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    # Contidional for server validation
    if request.method == "POST": # check if request method is post, submit form's data
        form = NewTaskForm(request.POST) # All data submitted saved it to form variable
        if form.is_valid(): # Chekc if form is valid
            task = form.cleaned_data["task"] # We take data from form, get the task ans saved it in task variable. 
            tasks.append(task) # Add task to my growing tasks list
            return HttpResponseRedirect(reverse("tasks:index")) # redirect back to index page once task is submited, using reverse function
        else:
            return render(request, "tasks/add.html", { # If not valid render the same data add.html and send back
                "form": form # passing it to form, to see errors
            })

    return render(request, "tasks/add.html", { # Otherwise if user just try to get only the page rather than sumbit data
        "form": NewTaskForm() # Get an empty form
        
    })