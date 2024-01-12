from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class candi_form(models.Model):
    name=models.CharField(max_length=24 ,null=True)
    city=models.CharField(max_length=24,null=True)
    job_desc=models.CharField(max_length=24,null=True)
    doj=models.DateField(null=True)
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Reject', 'Reject'),
        ('interviewed', 'interviewed'),
        ('--', '--'),
    ]
    status = models.CharField(max_length=12,choices=STATUS_CHOICES,default='--',null =True, blank=True)

def __str__(self):
        return self.candi_form

# employee registration model
class register_emp(models.Model):
      name=models.CharField(max_length=24)
      user_name=models.CharField(max_length=24)
      password=models.CharField(max_length=24)
      ROLE_CHOICES = [
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('operation', 'operation'),
        ('super_admin','super_admin'),
        ('agent','agent'),
        ('hr','hr')
        # Add more choices as needed
    ]
      role = models.CharField(max_length=24, choices=ROLE_CHOICES)


      