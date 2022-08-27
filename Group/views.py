from builtins import float

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from Friend.models import friends1,friendexpense
from Account.models import Account
from Group.models import groupmember,group_c,groupe
import random


# Create your views here.
def group(request):
    c = {}
    c.update(csrf(request))
    uname = request.session['email']
    ggname=[]
    gn=[]
    for i in groupmember.objects.all():
        if i.user == uname:
            str1 = i.groupdetails

            gn = str1.split('*')
            for i in gn:
                ggname.append(i)
    return render(request, 'home/group.html',{'ggname':ggname},c)

def group1(request):
    print ("yess")

    uname = request.session['email']
    gname = request.POST.get('gname','')
    ggname=[]
    gamount=[]
    gn=[]
    for i in groupmember.objects.all():
        if i.user == uname:
            str1 = i.groupdetails

            gn = str1.split('*')
            for i in gn:
                ggname.append(i)

    for i in group_c.objects.all():
        if i.gname == gname:
            if i.creater == uname:
                 return render(request, 'home/group.html', {'ggname':ggname,'msg': 'GroupName allready '})
    print (gname)
    f1 = request.POST.get('f1','')
    f2 = request.POST.get('f2','')
    f3 = request.POST.get('f3','')
    f4 = request.POST.get('f4','')
    f5 = request.POST.get('f5','')
    f6 = request.POST.get('f6','')
    f7 = request.POST.get('f7','')
    f8 = request.POST.get('f8','')
    f9 = request.POST.get('f9','')
    f10 =uname
    ff=[]
    if f1!="":
        ff.append(f1)
    if f2!="":
        ff.append(f2)
    if f3!="":
        ff.append(f3)
    if f4!="":
        ff.append(f4)
    if f5!="":
        ff.append(f5)
    if f6!="":
        ff.append(f6)
    if f7!="":
        ff.append(f7)
    if f8!="":
        ff.append(f8)
    if f9!="":
        ff.append(f9)
    if f10!="":
        ff.append(f10)
    for i in range(len(ff)):
        for j in range(i + 1, len(ff)):
            if ff[i] == ff[j]:
                return render(request,'home/group.html',{'ggname':ggname,'msg': 'Enter valid username'})

    def friendvery(f):
        if f == "":
            return 1
        for i in friends1.objects.all():
            if (i.user2 == f) & (i.user1 == uname):
                return 1
    a=friendvery(f1)
    b=friendvery(f2)
    c=friendvery(f3)
    d=friendvery(f4)
    e=friendvery(f5)
    f=friendvery(f6)
    g=friendvery(f7)
    h=friendvery(f8)
    i=friendvery(f9)
    z=0
    if a==b==c==d==e==f==g==h==i==1:
        z=1
    if z==0:
        return render(request,'home/group.html',{'ggname':ggname,'msg': 'Enter valid username'})
    print(f1)
    s=group_c(creater=uname,gname = gname,f1=f1,f2=f2,f3=f3,f4=f4,f5=f5,f6=f6,f7=f7,f8=f8,f9=f9,f10=f10)
    s.save()

    def finduser(f,c):
        for i in groupmember.objects.all():
            print(i.user)
            print("aaaaaaaaaa")
            print(f)
            if i.user == f:
                print("asdfghjkl")
                b = i.groupdetails
                if b == "":
                    c = gname
                else:
                    c= b + "*" + gname
        groupmember.objects.filter(user=f).update(groupdetails = c)
    finduser(f1,c)
    finduser(f2,c)
    finduser(f3,c)
    finduser(f4,c)
    finduser(f5,c)
    finduser(f6,c)
    finduser(f7,c)
    finduser(f8,c)
    finduser(f9,c)
    finduser(f10,c)
    ggname=[]
    gamount=[]
    gn=[]
    for i in groupmember.objects.all():
        if i.user == uname:
            str1 = i.groupdetails

            gn = str1.split('*')
            for i in gn:
                ggname.append(i)
    return render(request,'home/group.html',{'ggname':ggname,'msg': 'Group Added'})

def groupexp(request):
    gname = request.POST.get('gname', '')
    request.session['gname']=gname
    return render(request, "home/groupexe.html", {'gname': gname})


def groupexp1(request):
    uname = request.session['email']
    amo = request.POST.get('amount', '')
    type = request.POST.get('add', '')
    details = request.POST.get('details', '')
    gname = request.session['gname']
    print(uname)
    print(amo)
    print(details)
    print(gname)
    qq=groupe(ename=gname,pname=uname,detail=details,amount1=amo)
    qq.save()
    z=0
    for i in group_c.objects.all():
        if i.gname == gname:
            if i.f1 != "":
                z = z+1
            if i.f2 != "":
                z = z+1
            if i.f3 != "":
                z = z+1
            if i.f4 != "":
                z = z+1
            if i.f5 != "":
                z = z+1
            if i.f6 != "":
                z = z+1
            if i.f7 != "":
                z = z+1
            if i.f8 != "":
                z = z+1
            if i.f9 != "":
                z = z+1
            if i.f10 != "":
                z = z+1
            print(z)
            print(amo)
            amo1 = float(amo)
            amo = amo1/z
            print(amo)
            # th1= friends1.objects.all().filter(user1 = uname).filter(user2 = i.f1)
            # th1 = friends1.objects.get().filter(user1 = uname , user2 = i.f1)
            th1=friends1.objects.all()
            print("asdfg")
            print (th1)
            print("dfgh")
            th2  = th1.amount1
            th2 = th2 + amo
            th4 = -th1 + amo
            print("ewfdefuewgdyu")
            print(th1)
            friends1.objects.filter(user1 = uname , user2 = i.f1).update(amount1=th2)
            friends1.objects.filter(user1 = i.f1 , user2 = uname).update(amount1 =th4)
            return render(request, "home/group.html")