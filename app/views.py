from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from.models import master,student
# Create your views here.
def testview(request):
    req_method=request.method
    context={'usern':req_method}
    if req_method=='POST':
        usern=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=usern,password=psw)
        if user is not None:
            if usern=="master":
                return render(request, 'base.html', )
            elif usern=="student":
                return render(request, 'base2.html', )
            else:
                messages.error(request, 'invalid username or password')
                # context={'invalid':"invalid username or password"}
                return render(request, 'login.html', )


        else:
            messages.error(request,'invalid username or password')
            #context={'invalid':"invalid username or password"}
            return render(request, 'login.html',)
    else:
        return render(request,'login.html',context)

def input(request):
    req_method = request.method
    if req_method == 'POST':
        input = request.POST.get('input')
        sve = master(input=input)
        sve.save()
        return render(request, 'dashboard.html', )
    else:
        context = {'invalid': "not saved"}
        return render(request, 'dashboard.html', context)


def output(request,id):
    getdata=master.objects.get(id=id)
    req_method = request.method
    if req_method == 'POST':
        output = request.POST.get('output')
        getdata.output=output
        getdata.save()
        return render(request, 'stddashboard.html')
    else:
        context = {'invalid': "not saved"}
        return render(request, 'stddashboard.html', context)

def getques(request):
    getdata = master.objects.all().values()
    context = {'getdata': getdata}
    return render(request, 'getques.html', context)

def getdata(request):
    getdata = master.objects.all().values()
    context = {'getdata': getdata}
    return render(request, 'getdata.html', context)
def getdata2(request):
    getdata = master.objects.all().values()
    context = {'getdata': getdata}
    return render(request, 'getdata2.html', context)
def login(request):
    return redirect('/')