from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log")
        else:
            context["form"]=form
            return render(request, "register.html", context)
    return render(request,"register.html",context)

def login_page(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                # return redirect("cre")
                return render(request, "createreview.html")

            else:
                context["form"]=form
                return render(request, "login.html", context)
    return render(request,"login.html",context)

# def logout(request):
#     logout(request)
#     return redirect("log")

def CreateEmploy(request):
    if request.method=="POST":

        emp_name = request.POST['name']
        emp_designation = request.POST['designation']
        emp_employeid = request.POST['employeid']
        emp_phonenumber = request.POST['phonenumber']
        emp_email = request.POST['email']
        emp_rmp = request.POST['rmp']
        emp_age = request.POST['age']
        emp_salary = request.POST['salary']

        e = Employee()
        e.name = emp_name
        e.designation=emp_designation
        e.employeid=emp_employeid
        e.phonenumber=emp_phonenumber
        e.email=emp_email
        e.rmp=emp_rmp
        e.age=emp_age
        e.salary=emp_salary

        e.save()
    return render(request, 'create.html')

def FilterEmploy(request,id):
    em = Employee.objects.filter(id=id)
    context = {}
    context["em"] = em
    print(em)
    return render(request, "filter.html", context)












    




def list_employe(request):
    employ=Employee.objects.all()
    context={}
    context["employ"]=employ
    return render(request,"listemp.html",context)


def EditEmploy(request,id):
    em=Employee.objects.get(id=id)

    if request.method=="POST":
        context = {}
        context["em"] = em
        return render(request, "editemploy.html", context)
    else:
        return render(request,"listemp.html")




