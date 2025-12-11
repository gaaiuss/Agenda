from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    # messages.info(request, 'Any text')
    # messages.success(request, 'Any text')
    # messages.warning(request, 'Any text')
    # messages.error(request, 'Any text')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User registered')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login success')
            return redirect('contact:index')
        messages.error(request, 'Invalid login')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
