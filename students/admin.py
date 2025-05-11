from django.contrib import admin
from .models import Student


# Самый простой и быстрый способ добавить модель в админку
# admin.site.register(Student)

# Для более гибкой настройки отображения используется второй вариант
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year',)
    list_filter = ('year',)
    search_fields = ('first_name', 'last_name',)
