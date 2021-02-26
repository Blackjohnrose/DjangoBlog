from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    form = UserCreationForm()
    context = {
        'form': form,
        'title': 'register'
    }
    return render(request, 'users/register.html')
