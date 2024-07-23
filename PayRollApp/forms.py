from django import forms
from PayRollApp.models import Employee, OnSiteEmployees


# Creating form based model 

class EmployeeForm(forms.ModelForm):
      class Meta:
        model = Employee
        fields ="__all__"
        widgets={ # used to custimize type of inputfield
          "BirthDate":forms.widgets.DateInput(attrs={"type":"date","class":"form-control w-auto"}),
          "HireDate":forms.widgets.DateInput(attrs={"type":"date","class":"form-control w-auto"}),
          "FirstName":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "LastName":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "TitleName":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "Salary":forms.widgets.NumberInput(attrs={"class":"form-control w-auto"}),
          "Notes":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "HasPassport":forms.widgets.CheckboxInput(attrs={"class":"form-check-input"}),
          "Country":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "Email":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "Phone":forms.widgets.TextInput(attrs={"class":"form-control w-auto"}),
          "EmpDepartment":forms.widgets.Select(attrs={"class":"form-select w-auto"}),
          "EmpCountry":forms.widgets.Select(attrs={"class":"form-select w-auto"}),
        }
        
 
class OnSiteEmployeesForm(forms.ModelForm):
  class Meta:
    model = OnSiteEmployees
    fields = ['firstName','lastName','country','state','city']
    widgets={ # used to custimize type of inputfield
        
            "firstName":forms.widgets.TextInput(attrs={"class":"form-control w-25 my-1",
                                                      "placeholder":"First Name"}),
            
            "lastName":forms.widgets.TextInput(attrs={"class":"form-control w-25 my-1",
                                                      "placeholder":"Last Name"}),
            
            "country":forms.widgets.Select(attrs={"class":"form-select w-25 my-1",
                                                  }),
            
            "state":forms.widgets.Select(attrs={"class":"form-select w-25 my-1",
                                              }),
            
            "city":forms.widgets.Select(attrs={"class":"form-select w-25 my-1",
                                           }),
          }
  