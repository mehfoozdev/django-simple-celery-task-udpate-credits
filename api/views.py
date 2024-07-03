from django.shortcuts import render
from firstproject.celery import add
from api.tasks import sub
from celery.result import AsyncResult
from api.models import Student
from api.serializers import StudentSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


'''
Student API
'''
class StudentView(APIView):
    # permission_classes = [any]

    def get(self, request, format=None, id=None):
        if id is not None: 
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response({
                    'response' : 'Success',
                    'message' : 'Student record has been fetched.',
                    'data' : serializer.data
                }, status=status.HTTP_200_OK)
            except Exception as e :
                return Response({
                    'response' : 'failed',  
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            students = Student.objects.all()
            serializer  = StudentSerializer(students, many=True)
            return Response({
                'response' : 'Success',
                'message' : 'Students record has been fetched.',
                'data' : serializer.data
            }, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'response' : 'Success',
                'message' : 'Record has been saved.',
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'response' : 'Failed',
                'message' : 'Record not saved.',
                'error' : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)




# Display addition value after task execution
def index(request):
    result = add.delay(90, 30)
    return render(request, "api/home.html", {'result':result})


def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    print("Get: ", result.get())
    return render(request, 'api/result.html', {'result':result})