import time
import json

from celery import Celery
from db import getDocument
from task import Task

celery = Celery(__name__)
celery.config_from_object('celeryconfig')

@celery.task(name="create_task")
def create_task(input):
    task = Task(**(json.loads(input)))
    time.sleep(task.type * 10)
    return task.toJson()
