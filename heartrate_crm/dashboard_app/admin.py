from django.contrib import admin

# Register your models here.
from .models import candi_form , register_emp
admin.site.register(candi_form) 
admin.site.register(register_emp)
