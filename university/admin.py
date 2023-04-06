from django.contrib import admin
from .models import College
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name","clgid"]
    
admin.site.register(College)    