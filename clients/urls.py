from django.urls import path
from .views import index, create_employee


urlpatterns = [
    path('', index, name='client'),
    path('create-employee/<name>/', create_employee, name="create_employee")
]


