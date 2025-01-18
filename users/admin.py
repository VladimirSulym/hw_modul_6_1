from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'country',)
    list_filter = ('groups',)
    # search_fields = ('first_name', 'last_name',)