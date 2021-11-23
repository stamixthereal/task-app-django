from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = (
                    ('Frozen', 'Frozen'),
                    ('Done', 'Done'),
                    ('Undone', 'Undone')
                    )
                    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Name', max_length=255)
    task = models.TextField('Description')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
                            max_length=10,
                            choices=STATUS_CHOICES,
                            default='Undone')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'TASK'
        verbose_name_plural = 'TASKS'

class Message(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField('Body')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.__all__
