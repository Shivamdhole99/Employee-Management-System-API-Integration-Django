import requests
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

API_REGISTER_URL = "http://127.0.0.1:8000/api/register/"
API_LOGIN = "http://127.0.0.1:8000/api/login/"

# ================= REGISTER =================
def register_page(request):

    if request.method == "POST":

        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password")
        }

        response = requests.post(API_REGISTER_URL, json=data)

        if response.status_code == 201:
            return redirect("login")

    return render(request, "registration/register.html")


# ================= LOGIN =================
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post(
            API_LOGIN,
            json={
                "username": username,
                "password": password
            }
        )

        # ✅ LOGIN SUCCESS
        if response.status_code == 200:

            request.session['username'] = username

            return redirect('/addandshow/')   # ⭐ DASHBOARD

        else:
            return render(request, "registration/login.html",
                          {"error": "Invalid credentials"})

    return render(request, "registration/login.html")


# # ================= DASHBOARD =================
# def dashboard(request):

#     # ✅ check login session
#     if not request.session.get("username"):
#         return redirect("login")

#     return render(request, "dashboard.html")


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('login')