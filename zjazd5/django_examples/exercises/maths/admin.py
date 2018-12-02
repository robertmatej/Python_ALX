from django.contrib import admin
from maths.models import Math
# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["operation", 'wart1', 'wart2']      # dodaje dodatkowe pole do wyświetlenia
    search_fields = ['operation','','']      # pole do wyszyukiwania po danym parametrze
#    list_filter = ['oeration']


admin.site.register(Math,MathAdmin)         #w panelu admina mamy dostęp do wpisów w bazie dancyh

