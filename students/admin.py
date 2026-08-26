from django.contrib import admin

# Register your models here.

from .models import Student

# admin.site.register(Student) # Простое добавление

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """"""
    list_display = ('first_name', 'last_name', 'year',) # отображение
    list_filter = ('year',) # фильтрация по курсу
    search_fields = ('first_name', 'last_name',)