import json

import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import TaskForm
from .models import Tasks
from .serializers import TaskSerializer

# Create your views here.


def task_page(request):
    # Notice we are NOT passing context data usually
    # e.g. return render(request, 'tasks/tasks.html', {'tasks': tasks})
    # We just return the empty shell:
    return render(request, "tasks.html")


def hello_tasks(request):
    return render(request, "tasks.html", {"tasks": Tasks.objects.all()})


def add_task(request):
    # 1. If the user sent data (Clicked Submit)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # FIX: Use 'return', and use the URL name 'hello'
            return redirect("hello")

    # 2. If the user is just visiting the page (GET)
    else:
        form = TaskForm()

    # This indentation handles both the "GET" case
    # AND the "Invalid Form" case (e.g. empty title)
    return render(request, "add_task.html", {"form": form})


def delete_task(request, pk):
    task = Tasks.objects.get(id=pk)
    if task:
        task.delete()
    return redirect("hello")


# Add this to views.py
def edit_task(request, pk):
    # 1. Get the existing task (or crash if not found)
    task = Tasks.objects.get(id=pk)

    if request.method == "POST":
        # UPDATE: We pass 'instance=task' so Django knows to update, not create
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("hello")
    else:
        # LOAD: We pass 'instance=task' to pre-fill the form with existing data
        form = TaskForm(instance=task)

    # We can reuse the same template! Or make a new one called 'edit_task.html'
    return render(request, "edit_task.html", {"form": form})


@api_view(["GET"])
def task_list_api(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@csrf_exempt
def add_task_api(request):
    if request.method == "POST":
        try:
            # 1. Parse the incoming JSON
            data = json.loads(request.body)

            # 2. Create the task in the database
            # Ensure your model name is correct (Task vs Tasks)
            new_task = Tasks.objects.create(
                title=data["title"], content=data["content"], end_by=data["end_by"]
            )

            # 3. Send back success
            return JsonResponse(
                {"message": "Task created successfully", "id": new_task.id}, status=201
            )

        except Exception as e:
            # If JSON is bad or keys are missing, tell the user
            return JsonResponse({"error": str(e)}, status=400)

    # If the method is NOT POST, return an error
    return JsonResponse({"error": "POST request required"}, status=405)


@csrf_exempt
def edit_task_api(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        task = get_object_or_404(Tasks, pk=pk)
        try:
            task.title = data.get("title", task.title)
            task.content = data.get("content", task.content)
            task.end_by = data.get("end_by", task.end_by)
            task.is_done = data.get("is_done", task.is_done)
            task.in_progress = data.get("in_progress", task.in_progress)
            task.save()
            return JsonResponse({"message": "task updated successflly"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "PUT method required"}, status=405)


@csrf_exempt
def delete_task_api(request, pk):
    if request.method == "DELETE":
        task = get_object_or_404(Tasks, pk=pk)
        try:
            task.delete()
            return JsonResponse({"message": "deleted successfuly"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return JsonResponse({"error": "delete method required"}, status=405)
