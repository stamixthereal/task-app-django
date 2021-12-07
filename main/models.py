from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = (
                    ('Done', 'Done'),
                    ('Undone', 'Undone')
                    )
                    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Name', max_length=255)
    task = models.TextField('Description')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES, default='Undone')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'TASK'
        verbose_name_plural = 'TASKS'