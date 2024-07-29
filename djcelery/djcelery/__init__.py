# a way of setting up an approach to make the celery app available so that it can be
# utilised when running tasks in django.
from .celery import app as celery_app


__all__ = ("celery_app",)