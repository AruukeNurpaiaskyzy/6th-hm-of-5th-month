from django.contrib import admin

# Register your models here.
from .models import List
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'is_completed', 'created_at', 'image' ]