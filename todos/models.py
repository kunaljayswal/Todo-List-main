from django.db import models

from django.apps import AppConfig

class TodosConfig(AppConfig):
    name = 'todos'
    default_auto_field = 'django.db.models.BigAutoField'

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
