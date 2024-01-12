from django.shortcuts import render,redirect
from .models import candi_form , register_emp
from datetime import datetime


def index(request):
    return render(request,"home.html")





def submit(request):
    dt = candi_form.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        c_city = request.POST.get('city')
        c_job_desc = request.POST.get('job_desc')
        doj_str = request.POST.get('doj')         
        save_data = candi_form(name=name, city=c_city, job_desc=c_job_desc, doj=doj_str).save()
        return redirect(index)



def dashboard(request):
    dt=candi_form.objects.all()
    total_emp=register_emp.objects.all().count()
    count_all=candi_form.objects.all().count()


    context = {
        'data':dt,
        'count_all': count_all,
        'total_emp':total_emp
    }

    return render(request, 'index.html', context)

# this function use for register a employee


def register_employee(request):
    return render(request ,"register_employee.html")


def submit_emp_register(request):
    st = register_emp.objects.all()
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            role =  request.POST.get('role')       
            save_data = register_emp(name=name, user_name=user_name, password=password, role=role)
            save_data.save()
            msg = "Employee registered successfully"
            return render(request, 'register_employee.html', {"msg": msg})
    except Exception as e:
        e="Invalid Data entered"
        return render(request, 'register_employee.html', {"e": e})
