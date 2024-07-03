from rest_framework import serializers
from api.models import Student


'''
Defining Serializer
'''

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'semester', 'cgpa', 'last_semester_gpa', 'credits', 'address']