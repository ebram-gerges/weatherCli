import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterationSerializer, UserSerializer


def user_console(request):
    return render(request, "user_api_console.html")


@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()

    serialized = UserSerializer(users, many=True)

    return Response({"Users": serialized.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def register_user(request):
    serializer = UserRegisterationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(
            {"message": "success", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return JsonResponse({"message": "failed"}, status=status.HTTP_400_BAD_REQUEST)
