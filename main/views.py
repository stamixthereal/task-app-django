from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    """Rendering home page"""

    tasks = Task.objects.filter(user=request.user.id).order_by('-id')
    return render(request, 'main/index.html', {'title': 'My tickets', 'tasks': tasks})


@login_required
def new_task(request):
    """Rendering making a new task"""

    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            stock = form.save(commit = False)
            stock.user = request.user
            stock.save()
            return redirect('index')
        else:
            error = 'Wrong form!'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_task.html', context)


def register(request):
    """Rendering register function"""

    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            message = 'Something wrong...'
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form, 'message': message})


def mark_task_done(request, pk):
    """Changing tasks's status to Done"""

    task = Task.objects.get(id=pk)
    task.status = 'Done'
    task.save()
    return redirect('index')


def delete_task(request, pk):
    """Deleting task"""

    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('index')


class TaskDetailView(DetailView):
    """Details of each task"""

    model = Task
    template_name = 'main/detail.html'
    context_object_name = 'task'  