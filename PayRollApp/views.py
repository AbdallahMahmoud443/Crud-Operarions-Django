from django.shortcuts import render # type: ignore

from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employee  # type: ignore
from django.shortcuts import redirect # type: ignore
from django.core.paginator import Paginator,PageNotAnInteger # type: ignore
from django.conf import settings # type: ignore


def EmployeeList(request):
    # employees = Employee.objects.all() # To Get All Record In Table of Employee
    # ORM Doesn't execute query until you need data that is returned by this query (lazy loading)
    employees = Employee.objects.select_related('EmpDepartment','EmpCountry').all() # inner join (EmpDepartment & EmpCountry) => are forign keys
    # print(employees.query) # print query used
    pagePath = "PayRollApp/ShowEmployees.html"
    dict = {"employees":employees}
    return render(request,pagePath,dict)
    
def EmployeeDetails(request,id):
    # employee = Employee.objects.select_related('EmpDepartment','EmpCountry').get(id=id)
    employee = Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id=id) # filter return  List of object
    pagePath = "PayRollApp/EmployeeDetails.html"
    dict = {"employee":employee[0]} # Access First Record  That cause query will execute in database
    return render(request,pagePath,dict)
 
def EmployeeDelete(request,id):
    # To Show Information
    employee = Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id=id) # filter return  List of object
    pagePath = "PayRollApp/EmployeeDelete.html"
    dict = {"employee":employee[0]} # Access First Record  That cause query will execute in database
    # To Delete 
    if request.method == "POST":
       employee.delete()
       return redirect('ShowEmployeesPage') # redirect(name of url)
    return render(request,pagePath,dict)

def EmployeeUpdate(request,id):
    pagePath = "PayRollApp/EmployeeUpdate.html"
    employee = Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id=id) # filter return  List of object
    form = EmployeeForm(instance=employee[0])
    dict = {"form":form}
    if request.method =="POST":
        form = EmployeeForm(request.POST,instance=employee[0])
        if form.is_valid(): # validation in
            form.save()
            return redirect('ShowEmployeesPage') # redirect(name of url)
    return render(request,pagePath,dict)

def AddEmployee(request):
    pagePath = "PayRollApp/AddEmplyee.html"
    form = EmployeeForm()
    dict = {"form":form}
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid(): # validation in
            form.save()
            return redirect('ShowEmployeesPage') # redirect(name of url)
    return render(request,pagePath,dict)

# related with paginator
def PageWiseEmployeesList(request):
    page_size = int(request.GET.get('page_size',getattr(settings,'PAGE_SIZE',3))) # PAGE_SIZE =>variable in settings file or 5 by default
    page = request.GET.get('page',1)
    Employees = Employee.objects.select_related('EmpDepartment','EmpCountry').all()
    paginator = Paginator(Employees,page_size) 
    try:
        employees_page =paginator.page(page)
    except PageNotAnInteger:
        employees_page =paginator.page(1)
    return render(request,'PayRollApp/WiseEmployeesList.html',{
        'Employees_Page':employees_page,
        'page_size':page_size
    })
