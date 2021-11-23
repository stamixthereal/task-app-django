from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
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
    return render(request, 'users/register.html', {'form': form, 'message': message})