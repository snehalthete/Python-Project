from django.shortcuts import render,HttpResponse

from .models import customer

# Create your views here.
def index(request):
    return render(request,"index.html")

def registration(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]

        cus = customer(fname=fname, lname=lname)
        cus.save() # insert

        return HttpResponse("Registration successfully completed")
    else:
        return HttpResponse("Registration fail")