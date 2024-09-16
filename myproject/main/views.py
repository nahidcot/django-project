from django.shortcuts import render
from .models import Message

def home(request):
    # Retrieve the first message (or modify as needed)
    message = Message.objects.first()
    return render(request, 'home.html', {'message': message})
