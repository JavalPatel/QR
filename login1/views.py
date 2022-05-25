
from django.shortcuts import render, redirect
from login1.models import *
# Create your views here.
def login(request):
    user1 = request.POST.get('uname')
    passwd = request.POST.get('password')
    if passwd != None:        
        u_check = user.objects.filter(uname = user1)
        p_check = user.objects.filter(password = passwd)
        
        if u_check != "" and p_check != "":
            Name = u_check.values_list()
            print(Name)
            Name = Name[0][0]
            request.session['u_name'] = Name
            print()
            return redirect('/')
        
    return render(request, 'temp/login.html')
