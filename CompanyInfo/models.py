from django.db import models

# Create your models here.

class EmployeesInfo(models.Model):
    FirstName = models.CharField(max_length=20);
    LastName = models.CharField(max_length=20);
    job= models.CharField(max_length=10);
    
    
    

    