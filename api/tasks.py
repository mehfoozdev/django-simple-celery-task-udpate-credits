from celery import shared_task
from time import sleep
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from api.models import Student




@shared_task
def update_credits(*args, **kwargs):
    students = Student.objects.all()
    for student in students:
        student.credits += 500
        student.save()




@shared_task
def sub(x, y):
    sleep(10)
    return x - y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key

