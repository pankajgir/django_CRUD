from django.contrib import admin
from .models import student


@admin.register(student)

class studentAdmin(admin.ModelAdmin):
    list_display=['Id','name','email','course','city',]
