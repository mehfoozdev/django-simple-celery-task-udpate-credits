from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

app = Celery('firstproject')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

#Load task modules from all registered Django apps
app.autodiscover_tasks()


@app.task(name="addition_task")
def add(x, y):
    sleep(20)
    return x + y



# # Method 2 
# app.conf.beat_schedule = {
#         'every-10-seconds':{
#         'task':'myapp.tasks.clear_session_cache',
#         'schedule':10,
#         'args':('11111', )
#     }
#     # Add more periodic tasks as needed
# }

# # Using timedelta
# app.conf.beat_schedule = {
#         'every-10-seconds':{
#         'task':'myapp.tasks.clear_session_cache',
#         'schedule':timedelta(seconds=10),
#         'args':('11111', )
#     }
#     # Add more periodic tasks as needed
# }

# # Using timedelta
# app.conf.beat_schedule = {
#         'every-10-seconds':{
#         'task':'api.tasks.clear_session_cache',
#         'schedule':crontab(minute='*/1'),
#         'args':('11111', )
#     }
#     # Add more periodic tasks as needed
# }


# # Using timedelta
app.conf.beat_schedule = {
        'every-60-seconds':{
        'task':'api.tasks.update_credits',
        'schedule':crontab(minute='*/1'),
        'args':('11111', )
    }
    # Add more periodic tasks as needed
}