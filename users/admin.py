from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'phone', 'country',)
    # list_filter = ('year',)
    # search_fields = ('first_name', 'last_name',)