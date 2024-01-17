from django.shortcuts import render,redirect
from .models import candi_form , register_emp ,u_table
from datetime import date,datetime
from  django.contrib.auth import authenticate,login 
from  django.contrib.auth.models import User
from .form import cf_Form, cu_form
from django.contrib.admin.widgets import AdminDateWidget


def home(request):
    return render(request,"user_create.html")

def c_user(request):
    ud=u_table.objects.all()
    if request.method=="POST":
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sd=u_table(user_name=user_name,email=email,password=password).save()
        myuser=User.objects.create_user(user_name,email,password).save()
    return redirect(login)
    
def login_page(request):
    return render(request,"login.html")

def u_login(request):
    ud=u_table.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(dashboard)
        return redirect(home)



def index(request):
    return render(request,"home.html")


def submit(request):
    dt = candi_form.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        agent_name = request.POST.get('agent')   
        dob = request.POST.get('dob')  
        inusurance_id = request.POST.get('Insurance')   
        remark = request.POST.get('remark')      
        save_data = candi_form(name=name, contact=contact, address=address, dob=dob,inusurance_id=inusurance_id,remark=remark,agent_name=agent_name).save()
        return redirect(index)



def dashboard(request):
    dt=candi_form.objects.all()
    total_emp=register_emp.objects.all().count()
    count_all=candi_form.objects.all().count()
    # formatted_date = candi_form.objects.get("dob")
    context = {
        'data':dt,
        'count_all': count_all,
        'total_emp':total_emp,
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
            dob =  request.POST.get('dob')
            contact =  request.POST.get('contact')
            address =  request.POST.get('address')
            blood_group =  request.POST.get('blood_group')
            save_data = register_emp(name=name, user_name=user_name, password=password, role=role,contact=contact,  address=address, blood_group=blood_group, dob=dob)
            save_data.save()
            msg = "Employee registered successfully"
            return render(request, 'register_employee.html', {"msg": msg})
    except Exception as e:
        
        return render(request, 'register_employee.html', {"e": e})


def employee_table(request):
    st=register_emp.objects.all()
    
    return render(request,"employees.html",{'data':st})



#update 
def edit(request,id):
    data = candi_form.objects.get(id=id)
    form=cu_form()
    return render(request,'edit_form.html',{'form':form,"data":data})

    

def update(request,id):
    data = candi_form.objects.get(id=id)
    if request.method=="POST":
        rt = candi_form.objects.get(pk=id) 
        form = cf_Form(request.POST,instance=rt)
        if form.is_valid():
            form.save() 
            return redirect(dashboard)    
    return render(request,'edit_form.html',{'form':form,'data':data})


     

# delete data
def delete(request,id):
    data=candi_form.objects.get(id=id)
    data.delete()
    msg='deleted'
    return redirect(dashboard)









