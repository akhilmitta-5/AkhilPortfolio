from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Contact


def home(request):
    return render(request, 'index.html')


@require_POST
def contact(request):

    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        messages.error(request, 'Please fill all fields.')
        return redirect('home')

    if len(name) > 100 or len(message) > 5000:
        messages.error(request, 'Input is too long.')
        return redirect('home')

    Contact.objects.create(
        name=name,
        email=email,
        message=message
    )

    messages.success(
        request,
        'Your message was submitted successfully!'
    )

    return redirect('home')
