import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    emp_designation = django_filters.CharFilter(field_name='emp_designation', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['emp_designation']