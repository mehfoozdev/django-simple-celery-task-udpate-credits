from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    semester = models.CharField(max_length=100)
    cgpa = models.FloatField()
    last_semester_gpa = models.FloatField()

    credits = models.IntegerField()
    address = models.CharField(max_length=255, null=True, blank=True, default='')

    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name