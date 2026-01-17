from django.urls import include, path

from .views import (
    add_task,
    add_task_api,
    delete_task,
    delete_task_api,
    edit_task,
    edit_task_api,
    hello_tasks,
    task_list_api,
    task_page,
)

urlpatterns = [
    path("", task_page, name="task_page"),
    path("add_task", add_task, name="add_task"),
    path("delete_task/<int:pk>", delete_task, name="delete_task"),
    path("edit_task/<int:pk>", edit_task, name="edit_task"),
    path("api/tasks/", task_list_api, name="tasks_api"),
    path("api/add_task/", add_task_api, name="add_task_api"),
    path("api/edit_task/<int:pk>/", edit_task_api, name="edit_task_api"),
    path("api/delete_task/<int:pk>/", delete_task_api, name="delete_task"),
]
