from home.views import index, person_list, student_view, student_details
#from employee.views import Employees, EmployeeDetails
from employee.views import EmployeeViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('index/', index),
    path('person/', person_list),
    path('students/', student_view),
    path('students/<int:pk>/', student_details),

    # urls for all except viewsets 
    # path('employee/', Employees.as_view()),
    # path('employee/<int:pk>/', EmployeeDetails.as_view()),

    #viewset
    path('', include(router.urls))

]
