from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['rest_api', 'django', 'fastapi'],
        'course_provider' : 'Self_learning'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print('You Hit a GET Method')
        return Response(courses)
    
    elif request.method == 'POST':
        data = request.data
        print('************')
        print(data)
        print('You hit POST method')
        return Response(courses)
    
    elif request.method == 'PUT':
        print('You hit PUT method')
        return Response(courses)

@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


