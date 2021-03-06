from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):

    STATUS_CHOICES = (
                    ('Done', 'Done'),
                    ('Undone', 'Undone')
                    )
                    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Name', max_length=60)
    task = models.TextField('Description')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Undone')

    def __str__(self):
        return self.title

    def mark_as_done(self):
        self.status = 'Done'
        self.save()

    class Meta:
        verbose_name = 'TASK'
        verbose_name_plural = 'TASKS'