from django.contrib import admin
from App.models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['title','first_name','last_name','mobile','card_id_no','email','gender','age','address','created_at']
    search_fields = ['first_name','last_name','email','age']
    list_filter = ['gender']
    list_per_page = 10    
admin.site.register(Staff,StaffAdmin)