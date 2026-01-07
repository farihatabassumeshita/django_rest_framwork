from rest_framework import serializers
from .models import Person, Student

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'