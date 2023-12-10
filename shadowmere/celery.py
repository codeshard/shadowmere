import os

from celery import Celery

if os.getenv("DEBUG") == "True":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shadowmere.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shadowmere.settings.prod")

app = Celery("shadowmere")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
