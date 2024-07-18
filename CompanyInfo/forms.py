from django.forms import modelform_factory # type: ignore
from CompanyInfo.models import EmployeesInfo
from django import forms






# So this model form factory helps you to generate the forms dynamically.
EmployeeInfoForm = modelform_factory(EmployeesInfo,fields=['FirstName','LastName','job']) # Return list of forms


# this class to change required attribute to none and customize inputs in modelform_factory list
class DynamicEmployeeInfoForm(EmployeeInfoForm):
    def __init__(self,*args,**kwargs):
        super(DynamicEmployeeInfoForm,self).__init__(*args,**kwargs)
        # deactivate require validation of fields
        for field in self.fields.values():
            field.widget.attrs.pop('required',None)
            
            

# Second way for bulk insert 
class DynamicEmployeeInfoFormNew(forms.ModelForm):
    class Meta:
        model = EmployeesInfo
        fields ='__all__'
        
EmployeeInfoFormSet = forms.modelformset_factory(EmployeesInfo,
                                                 form=DynamicEmployeeInfoFormNew,
                                                 extra=5)