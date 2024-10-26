from django.contrib import admin

# Register your models here.
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name','phone', 'created_at', 'age']