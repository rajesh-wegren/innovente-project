from django.contrib import admin
from employeeapp.models import Member_inno,Address
# Register your models here.
# admin.site.register(Member_inno),
admin.site.register(Address),



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth','designation')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'designation')

admin.site.register(Member_inno, EmployeeAdmin)