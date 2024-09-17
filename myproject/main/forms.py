from django import forms
from .models import ProfitCalculation

class ProfitCalculationForm(forms.ModelForm):
    class Meta:
        model = ProfitCalculation
        fields = '__all__'
