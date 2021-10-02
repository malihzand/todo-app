from django.contrib import admin
from .models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['work', 'owner']


admin.site.register(TodoItem, TodoItemAdmin)
