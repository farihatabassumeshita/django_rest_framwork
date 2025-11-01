from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['rest_api', 'django', 'fastapi'],
        'course_provider' : 'Self_learning'
    }
    return Response(courses)
