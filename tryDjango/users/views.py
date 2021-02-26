from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#20:02

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'title': 'register'
    }
    return render(request, 'users/register.html', context)
