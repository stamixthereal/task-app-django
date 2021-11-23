from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user.id)
    return render(request, 'main/index.html', {'title': 'My tickets', 'tasks': tasks})

@login_required
def new_ticket(request):
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
    return render(request, 'main/new_ticket.html', context)