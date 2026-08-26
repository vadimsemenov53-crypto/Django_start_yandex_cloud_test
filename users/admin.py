from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number',)
    list_filter = ('username',)
    search_fields = ('email', 'username',)
    exclude = ('password',)