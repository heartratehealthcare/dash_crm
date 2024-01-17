from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class candi_form(models.Model):
    name=models.CharField(max_length=24 ,null=True)
    contact=models.CharField(max_length=24,null=True)
    address=models.CharField(max_length=24,null=True)
    dob=models.DateField(null=True)
    inusurance_id = models.CharField(max_length=10,default='',null =True)
    remark = models.CharField(max_length=45,default='',null =True)
    agent_name=models.CharField(max_length=24,null=True)
    m_file = models.FileField(upload_to='documents/',null=True)
    status = models.TextField(default='',null=True)

    def __str__(self):
        return self.name
    



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
      role = models.CharField(max_length=24, choices=ROLE_CHOICES,default="agent")
      contact=models.CharField(max_length=24,default="")
      address=models.TextField(default="")
      blood_group=models.CharField(max_length=10,default="")
      dob= models.DateField(null=True)
      

class u_table(models.Model):
      user_name=models.CharField(max_length=24)
      email=models.CharField(max_length=24)
      password=models.CharField(max_length=24)