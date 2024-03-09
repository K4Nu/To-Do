from django.shortcuts import render, HttpResponse,redirect
from .forms import TaskForm
from .models import Task


def index(request):
    tasks=Task.objects.all()
    return render(request,"task/index.html",{"tasks":tasks})

def task_form(request):
    if request.method == "POST":
        form = TaskForm(request.POST)  # Initialize form with POST data
        if form.is_valid():
            date_start=form.cleaned_data["date_start"]
            date_end=form.cleaned_data["date_end"]
            if date_start>date_end:
                form.add_error("date_end","End date should be after date")
            else:
                form.save()
                return redirect("index")
    else:
        form = TaskForm()  # Create an empty form instance for a GET request

    return render(request, "task/form.html", {"form": form})
