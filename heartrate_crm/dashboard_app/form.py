from django import forms  
from .models import candi_form 
from django.contrib.admin.widgets import AdminDateWidget


class cf_Form(forms.ModelForm):
    class Meta:  
        model = candi_form  
        fields = '__all__'
        Widgets={
            "dob":AdminDateWidget()
        }
class cu_form(forms.Form):
    name=forms.CharField(max_length=25)
    contact=forms.CharField(max_length=24)
    address=forms.CharField(max_length=24)
    dob=forms.DateField(widget=AdminDateWidget())
    inusurance_id = forms.CharField(max_length=10)
    remark = forms.CharField(max_length=45)
    agent_name=forms.CharField(max_length=24)
    m_file = forms.FileField()
    status = forms.CharField(max_length=56)