from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from.models import *


def home(request):
    return render(request,"todo.html")

def rejalar(request):
    if request.user.is_authenticated:

        if request.method=='POST':

            Rejalar.objects.create(
                sarlavha=request.POST.get("s_v"),
                batafsil=request.POST.get("b"),
                sana=request.POST.get("s"),
                student=Student.objects.get(user=request.user),

            )
            return redirect("/rejalar/")

    s1=Student.objects.get(user=request.user)
    data={
        "rejalar":Rejalar.objects.filter(student=s1),

    }
    return render(request,'todo.html', data)

def loginView(request):
    if request.method=='POST':
        users=authenticate(username=request.POST.get("l"), password=request.POST.get("p"))
        if users is None:
            return redirect("/")
        login(request, users)
        return redirect("/rejalar/")


    return render(request, 'login.html')
def logoutView(request):
    logout(request)
    return redirect("/")
def reja_ochir(request, pk):
    t=Rejalar.objects.get(id=pk)
    if Student.objects.get(user=request.user)==t.student:
        t.delete()
    return redirect("/rejalar/")



def reja_edit(request, pk):
    if request.method == 'POST':
        if request.POST.get("b_n") == 'on':
            bajarilmagani = True
        else:
            bajarilmagani = False
        Rejalar.objects.filter(id=pk).update(
            sarlavha=request.POST.get("s_v"),
            batafsil=request.POST.get("b"),
            sana=request.POST.get("s"),
            bajarilmagan=bajarilmagani,

        )
        return redirect("/rejalar/")
    data={
        "plans":Rejalar.objects.get(id=pk)
    }
    return render(request, "todo_edit.html", data)
def bajarilmagan_rejalar(request):
    data={
        "rejalar":Rejalar.objects.filter(bajarilmagan=False)
    }
    return render(request, 'bajarilmagan.html', data)



def register(request):
    if request.method=='POST':
        u=User.objects.create_user(
            username=request.POST.get('login'),
            password=request.POST.get('parol'),
        )
        Student.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            st_raqam=request.POST.get('st_r'),
            user=u
        )
        return redirect('/')
    return render(request, 'register.html')

