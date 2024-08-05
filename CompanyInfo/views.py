from django.shortcuts import render # type: ignore
from CompanyInfo.forms import EmployeeInfoForm, EmployeeInfoFormSet
from CompanyInfo.models import EmployeesInfo
from django.shortcuts import redirect # type: ignore
from django.db import transaction
# Create your views here.

# insert Mutiple Employee at one time 
def BulkInsertEmployess(request):
    extra_forms = 5
    # use list because DynamicEmployeeInfoForm return list for forms
    forms = [EmployeeInfoForm(request.POST or None,prefix=f'employee-{i}') for i in range(extra_forms)] 
    status =''
    if request.method =='POST':
       for form in forms:
           if form.is_valid() and form.cleaned_data.get('FirstName',''): # to get any values of form,form must bet valid first
                form.save()
                status = 'Records were Inserted Successfully'
    return render(request,'CompanyInfo/BulkInsert.html',{'forms':forms,
                                    'extra_forms':range(extra_forms),
                                    'status':status})

# second way for bulk inseting 
def BulkInsertEmployessNew(request):
    # GET request
    formset = EmployeeInfoFormSet(queryset=EmployeesInfo.objects.none(),prefix='employee') # to reset values of form with empty values
    if request.method =="POST":
        formset = EmployeeInfoFormSet(request.POST,prefix='employee')
        if formset.is_valid():
            employees = formset.save(commit=False) # don't commit data to database directly
            EmployeesInfo.objects.bulk_create(employees) # save all employees at one time used bulk_create method
            return redirect('bulkInsertNewPage') # name of url       
    return render(request,'CompanyInfo/BulkInsertNew.html',{'formset':formset})

# Update Employees
def BulkUpdateEmployee(request):
    employees= EmployeesInfo.objects.all();
    forms = [EmployeeInfoForm(request.POST or None,instance=employee,prefix=f'employee-{employee.id}') for employee in  employees]
    if request.method == 'POST':
        update_employees =[]
        for form in forms:
            if form.is_valid():
               employee = form.instance # employee Object
               # override old values of form
               employee.FirstName = form.cleaned_data.get('FirstName') # form value
               employee.LastName = form.cleaned_data.get('LastName')# form value
               employee.job = form.cleaned_data.get('job')# form value
               update_employees.append(employee) # update_employees is list of employees
        EmployeesInfo.objects.bulk_update(update_employees,fields=['FirstName','LastName','job'])
        return redirect('bulkUpdatePage')
    return render(request,'CompanyInfo/BulkUpdate.html',{'forms':forms,'employees':employees})

# Bulk Delete with CheckBox
def ListOfEmployees(request):
    employees = EmployeesInfo.objects.all();
    pagePath = 'CompanyInfo/ListEmployees.html'
    if request.method == "POST":
        selected_ids = request.POST.getlist('select_ids') # list of ids
        if selected_ids:
            EmployeesInfo.objects.filter(pk__in=selected_ids).delete()  # selected_ids => list
            return redirect('bulkDeletePage')
        
    return render(request,pagePath,{'employees':employees})

# Bulk Delete with Radio Button
def BulkDeleteDemoRadioButton(request):
    employees = EmployeesInfo.objects.all();
    if request.method =="POST":
        employee_id = request.POST.get('select_ids')
        EmployeesInfo.objects.filter(pk=employee_id).delete() # employee_id => one value
        return redirect('bulkDeleteRadioPage')
    return render(request,'CompanyInfo/Bulkdelete.html',{'employees':employees})

def TransactionDemo(request):
    try:
        with transaction.atomic(): 
            '''
            transaction.atomic => anything cause error all transaction will rollback 
            don't excuted in database  (this is very important)
            example : if you work (updated & insert data ) in two depending table in same time
            in cause of error no sql statement execute in database
            '''  
            employee = EmployeesInfo.objects.create(FirstName="Adam",LastName="Abdallah",job="Doctor")
            employee = EmployeesInfo.objects.create(FirstName="Hossam",LastName="mohamed",job="Accountant")
            employee = EmployeesInfo.objects.create(FirstNames="Sayed",LastName="nagy",job="Teacher")
            employee = EmployeesInfo.objects.create(FirstName="Sara",LastName="Habibe",job="nurse")
            employee = EmployeesInfo.objects.create(FirstName="Nour",LastName="Ahmed",job="officer")
            employee = EmployeesInfo.objects.create(FirstName="Hassan",LastName="Ali",job="pilot")
    except Exception as e:
        return render(request,'CompanyInfo/TransactionDemo.html',{'Message':str(e)})
    return render(request,'CompanyInfo/TransactionDemo.html',{'Message':'success'})

