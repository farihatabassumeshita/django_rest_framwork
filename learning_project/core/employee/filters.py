import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    emp_designation = django_filters.CharFilter(field_name='emp_designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    emp_id = django_filters.RangeFilter(field_name='emp_id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label= 'From Emp ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To Emp ID')

    class Meta:
        model = Employee
        fields = '__all__'

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset