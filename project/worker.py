import os
import time

from celery import Celery


celery = Celery(__name__)
celery.config_from_object('celeryconfig')

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
