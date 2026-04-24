from django.contrib import admin
from .models import Boxer

class BoxerAdmin(admin.ModelAdmin):
    list_display=('fullname', 'hp', 'strongest_attack') 
    ordering = ('strongest_attack',)
    search_fields = ('fullname', 'strongest_attack')
    list_filter = ('strongest_attack',)
admin.site.register(Boxer, BoxerAdmin)