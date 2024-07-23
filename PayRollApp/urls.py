from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('showemployees',views.EmployeeList,name="ShowEmployeesPage"),
    path('employeedetails/<int:id>',views.EmployeeDetails,name="EmployeeDetailsPage"),
    path('deleteemployee/<int:id>',views.EmployeeDelete,name="DeleteEmployeePage"),
    path('updateemployee/<int:id>',views.EmployeeUpdate,name="UpdateEmployeePage"),
    path('addemployee',views.AddEmployee,name="AddEmployeePage"),
    path('wiseemployees',views.PageWiseEmployeesList,name="wiseEmployeesPage"),
    path('cascadingselect/',views.cascadingSelect,name="cascadingSelectPage"),
    path('loadstate/',views.load_states,name='load_states'),
    path('loadcity/',views.load_Cities,name='load_cities'),
]
