from django.contrib import admin
from .models import Adopcion

class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'observaciones')

admin.site.register(Adopcion, AdopcionAdmin)