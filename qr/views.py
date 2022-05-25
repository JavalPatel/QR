from django.http import HttpResponse
from django.shortcuts import render
from qr.py_qr.qr import qr
from login1.models import *


def index(request):
    return render(request, "temp/index.html")

def qr_view(request):
    #name = request.POST.get("name", "Patel Javal Kalpeshbhai")
    amount = str(request.POST.get("amount", "None"))
    #upi_id = request.POST.get("upi_id", "6351489115@paytm")
    if 'u_name' in request.session:
        u_name = request.session['u_name'] 
    print(u_name) 
    get_d = info.objects.get(uname = u_name)
    name = get_d.name
    upi_id = get_d.upi_id
    print(upi_id)
    if amount != "None" :
        qr(upi_id, name, amount)
    details = {"upi_id": upi_id, "name": name}

    return render(request, "temp/qr.html", details)