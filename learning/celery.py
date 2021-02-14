from __future__ import absolute_import ,unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')
# to let know celery the project name
app = Celery('learning')


# add django setting module as a configuration source for celery
app.config_from_object('django.conf:settings',namespace='CELERY')

# to autodiscover tasks that we might have in our app
app.autodiscover_tasks()