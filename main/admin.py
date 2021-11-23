from django.contrib import admin
from .models import Task


@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'task', 'status')
    list_filter = ('status', 'publish')