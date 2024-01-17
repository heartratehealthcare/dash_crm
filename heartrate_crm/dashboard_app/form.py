from django import forms  
from .models import candi_form 
from django.contrib.admin.widgets import AdminDateWidget


class cf_Form(forms.ModelForm):
    class Meta:  
        model = candi_form  
        fields = '__all__'
