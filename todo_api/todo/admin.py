from django.contrib import admin
from .models import Status, Todo

admin.site.register(Todo)
admin.site.register(Status)