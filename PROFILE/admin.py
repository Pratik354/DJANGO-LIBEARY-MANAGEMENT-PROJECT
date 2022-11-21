from django.contrib import admin
from PROFILE.models import profile

class RegisAdmin(admin.ModelAdmin):
    list_display=("user","stud_id","number","gender","dob","branch","semister","date","photo")
admin.site.register(profile,RegisAdmin)