
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User  

def agent_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user = User.objects.filter(uname=user_name, upass=user_pass).first()
        return render(request, 'agent_login.html')