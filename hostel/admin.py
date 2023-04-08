from django.contrib import admin
from .models import Hostel
# Register your models here.
class Hostelview(admin.ModelAdmin):
    list_display=["room_id","count"]
    search_fields=["room_id"]

admin.site.register(Hostel,Hostelview)