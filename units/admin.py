from django.contrib import admin
from .models import DepartmentalUnit

@admin.register(DepartmentalUnit)
class DepartmentalUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)