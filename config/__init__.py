from __future__ import absolute_import, unicode_literals

from celery import Celery

# Это позволит убедиться, что приложение всегда импортируется, когда запускается Django
from config.celery import app as celery_app

__all__ = ('celery_app',)
celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    broker_connection_retry=False,
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=10,
)