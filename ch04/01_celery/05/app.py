
from celery import Celery
import celeryconfig

app = Celery(__name__, include=["tasks"])

app.config_from_object(celeryconfig)
