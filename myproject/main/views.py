from django.shortcuts import render
from .models import Message
from .forms import ProfitCalculationForm

def home(request):
    # Retrieve the first message (or modify as needed)
    message = Message.objects.first()
    return render(request, 'home.html', {'message': message})


def calculate_profit(request):
    if request.method == 'POST':
        form = ProfitCalculationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ProfitCalculationForm()
    return render(request, 'calculate_profit.html', {'form': form})