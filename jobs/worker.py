from celery import Celery

from jobs import celeryconfig

celery_app = Celery("celeryExample")
celery_app.config_from_object(celeryconfig)
