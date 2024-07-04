from django.db import models # type: ignore

# Create your models here.
class Departments(models.Model):
    DeprtName = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.DeprtName # importatnt to show name of options


class Countries(models.Model):
    CountryName = models.CharField(max_length=30)
    def __str__(self):
        return self.CountryName # importatnt to show name of options
    
    
class Employee(models.Model):
    """COUNTRIES =[
        ("IND", "INDIA"),
        ("USA", "United States Of America"),
        ("UK", "United Kingdom"),    
        ("AUS", "AUSTRALIA"),
        ("AU", "AUSTRIA"),
        ("SP", "SPAIN"),
        ("EG", "EGYPT"),    
    ]"""
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    TitleName = models.CharField(max_length=30)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    BirthDate = models.DateField()
    HireDate = models.DateField()
    Notes = models.CharField(max_length=200)
    # Country = models.CharField(choices=COUNTRIES,max_length=40,default=None)
    Email = models.CharField(default="",max_length=50)
    Phone =models.CharField(default="",max_length=12)
    EmpDepartment = models.ForeignKey("Departments",default=0,on_delete=models.PROTECT,related_name="Employee_Department")
    EmpCountry=models.ForeignKey("Countries",default="",on_delete=models.PROTECT,related_name="Employee_Country")
    
    def __str__(self):
        return self.FirstName +' '+ self.LastName
