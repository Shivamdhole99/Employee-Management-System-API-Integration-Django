import requests
from django.shortcuts import render, redirect

from .models import employee
from django.contrib import messages
# from .forms import EmployeeForm

API_URL = "http://127.0.0.1:8000/api/employees/"

import requests
from django.shortcuts import render, redirect

API_URL = "http://127.0.0.1:8000/api/employees/"


def addandshow(request):

    username = request.session.get("username")

    # ---------- ADD EMPLOYEE ----------
    if request.method == "POST":
        data = {
            "username": username,
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "department": request.POST.get("department"),
            "salary": request.POST.get("salary"),
        }

        requests.post(API_URL, json=data)
        return redirect("addandshow")

    # ---------- SHOW USER EMPLOYEES ----------
    response = requests.get(f"{API_URL}?username={username}")

    employees = []

    if response.status_code == 200:
        employees = response.json()

    return render(request, "addandshow.html", {
        "employees": employees,
        "username": username
    })

def update_data(request, id):

    API_URL = f"http://127.0.0.1:8000/api/employees/{id}/"

    if request.method == "POST":

        data = {
            "name": request.POST['name'],
            "email": request.POST['email'],
            "department": request.POST['department'],
            "salary": request.POST['salary'],
        }

        requests.put(API_URL, json=data)

        return redirect('addandshow')

    response = requests.get(API_URL)
    employee = response.json()

    return render(request, "update.html",
                  {"employee": employee})


def delete_data(request, id):

    requests.delete(f"{API_URL}{id}/")

    return redirect('/')
