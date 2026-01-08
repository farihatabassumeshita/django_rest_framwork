from home.views import index, person_list, student_view, student_details
from employee.views import Employees, EmployeeDetails
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person_list),
    path('students/', student_view),
    path('students/<int:pk>/', student_details),

    path('employee/', Employees.as_view()),
    path('employee/<int:pk>/', EmployeeDetails.as_view()),

]
