from django.shortcuts import render # type: ignore

from PayRollApp.forms import EmployeeForm, OnSiteEmployeesForm
from PayRollApp.models import City, Employee, State  # type: ignore
from django.shortcuts import redirect # type: ignore
from django.core.paginator import Paginator,PageNotAnInteger # type: ignore
from django.conf import settings # type: ignore
from django.db.models import Q # type: ignore
from django.http import JsonResponse

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
    search_query = request.GET.get('search','')
    # this query related with sort functionality
    '''
    #! Wrong Code For Sorting
    # this to query parameter is required for sortable libarary of sortable at same syntax => (sort_by,sort_order)
    sort_by = request.GET.get('sort_by','id') # => columns
    sort_order=request.GET.get('sort_order','asc') # => ordering
    
    # validation on keyword of sorting (columns)
    valid_sort_fields = ['id','FirstName','Salary','Hire Data']
    if sort_by not in valid_sort_fields :
       sort_by = 'id'
    '''
    
    # 1-this code is related with search functionality 
    Employees = Employee.objects.filter(
                                        Q(id__icontains=search_query) |
                                        Q(FirstName__icontains=search_query) |
                                        Q(LastName__icontains=search_query) |
                                        Q(Salary__icontains=search_query))
    '''
    #! Wrong Code For Sorting 
    # 2-Apply Soring Code (ordering)
    if sort_order == 'desc':
       Employees.order_by(f'-{sort_by}') # nigative sign is denote desc ordering 
    else:
       Employees.order_by(sort_by)
    '''
    #Employees = Employee.objects.select_related('EmpDepartment','EmpCountry').all()
    paginator = Paginator(Employees,page_size) 
    try:
        employees_page =paginator.page(page)
    except PageNotAnInteger:
        employees_page =paginator.page(1)
    return render(request,'PayRollApp/WiseEmployeesList.html',{
        'Employees_Page':employees_page,
        'page_size':page_size,
        'search_query':search_query,
        #'sort_by':sort_by,
        #'sort_order':sort_order
    })


# Cascading DropDown List
def cascadingSelect(request):
    employeeForm = OnSiteEmployeesForm()
    if request.method =="POST":
        employeeForm = OnSiteEmployeesForm(request.POST)
        if employeeForm.is_valid():
           employeeForm.save()
           return JsonResponse({'success':True})
    return render(request,'PayRollApp/cascadingSelect.html',{'form':employeeForm})

def load_states(request):
    country_id = request.GET.get('country_id')
    print(country_id)
    state = State.objects.filter(country_id=country_id).values('id','name') # id & name => columns names in State table
    print(list(state))
    return JsonResponse(list(state),safe=False)

def load_Cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id','name') # id & name => columns names in State table
    return JsonResponse(list(cities),safe=False) # safe => realted with script injection
    
    
    

