from django.urls import include, path

from .views import get_all_users, register_user, user_console

urlpatterns = [
    path("console/", user_console, name="user_console"),
    path("api/get_users/", get_all_users, name="list_users"),
    path("api/create_user/", register_user, name="register_user"),
]
