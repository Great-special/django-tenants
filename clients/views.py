from django.shortcuts import render

from django.http import HttpResponse
from .models import Employee

# Create your views here.


def index(request):
    return HttpResponse(f"<h1>This is {request.tenant}</h1>")


def create_employee(request, name):
    employee = Employee.objects.create(name=name)
    employee.save()
    
    return HttpResponse(f"<h1>{request.tenant} employee created.</h1>")