from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer


# ✅ REGISTER API
@api_view(['POST'])
def register_api(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User Created"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


# ✅ LOGIN API
@api_view(['POST'])
def login_api(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "message": "Login successful",
            "username": user.username
        })

    return Response(
        {"error": "Invalid credentials"},
        status=status.HTTP_400_BAD_REQUEST
    )