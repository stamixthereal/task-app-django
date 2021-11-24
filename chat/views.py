from django.db import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Task
from django.views.generic.detail import DetailView


class TaskDetailView(DetailView):
    model = Task
    template_name = 'chat/detail.html'
    context_object_name = 'task'