from django.contrib import admin # type: ignore

from PayRollApp.models import Countries, Departments, Employee

# Register your models here.


admin.site.register(Employee) # To Show Your Employee Model in Admin Panel
admin.site.register(Departments) # To Show Your Employee Model in Admin Panel 
admin.site.register(Countries) # To Show Your Employee Model in Admin Panel 