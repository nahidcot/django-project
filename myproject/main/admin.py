from django.contrib import admin
from .models import Message
from .models import ProfitCalculation

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(ProfitCalculation)