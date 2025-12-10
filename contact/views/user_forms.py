from django.contrib import messages
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
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )
