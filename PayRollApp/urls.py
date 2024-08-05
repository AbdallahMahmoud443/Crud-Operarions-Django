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
    path('cookie',views.cookie_page,name='Cookie_Page'),
    path('addcookie',views.add_cookie,name='add_Cookie_Page'),
    path('clearcookie',views.clear_cookies,name='clear_Cookie_Page'),
    path('viewcookie/<str:cookie_name>',views.view_cookie,name='View_Cookie_Page'),
    path('deletecookie/<str:cookie_name>',views.delete_cookie,name='Delete_Cookie_Page'),
]
