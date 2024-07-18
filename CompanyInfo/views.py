from django.shortcuts import render # type: ignore
from CompanyInfo.forms import EmployeeInfoForm, EmployeeInfoFormSet
from CompanyInfo.models import EmployeesInfo
from django.shortcuts import redirect # type: ignore

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