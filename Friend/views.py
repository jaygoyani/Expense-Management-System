from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from Friend.models import friends1,friendexpense
from Account.models import Account

def fri1(request):
    return render(request, "add.html")


def add1(request):
    print('in login')
    uname = request.session['email']
    friamount=[]
    fri = []
    amount = []
    for i in friends1.objects.all():
        if uname == i.user1:
            fri.append(i.user2)
            st = str(i.amount1)
            amount.append(st)
            print(amount)
    itmes = friends1.objects.all().filter(user1=request.session['email'])

    # for i in friends1.objects.all():
    #     if uname == i.user1:
    #         x=i.user2
    #         st =i.amount1
    #         friamount.append(x)
    #         friamount.append(st)
    # print("add1")
    # print(friamount)


    uname = request.session['email']
    uname1 = request.POST.get('friend_name','')
    for i in friends1.objects.all():
        if uname == i.user1:
            if uname1 == i.user2:
                return render(request,"home/friendsadd.html",{'itmes':itmes ,'msg':'You are already friends'})
    v = 1
    for i in Account.objects.all():
        if uname1 == i.email:
            v = 0
    if v == 1:
        return render(request, "home/friendsadd.html", {'itmes':itmes ,'msg': 'Enter valid username'})
    if uname1 == uname:
        return render(request,"home/friendsadd.html",{'itmes':itmes ,'msg':'Enter valid username'})
    if uname1 == '':
        return render(request,"home/friendsadd.html",{'itmes':itmes ,'msg':'Enter valid username'})
    s = friends1(user1 = uname,user2 = uname1,)
    s.save()
    v = friends1(user1 = uname1 , user2 = uname)
    v.save()
    return HttpResponseRedirect('/Friend/',{'itmes':itmes ,'msg': 'You are now friends'})

def add(request):
    c = {}
    c.update(csrf(request))
    uname = request.session['email']
    friamount=[]
    fri=[]
    amount=[]
    for i in friends1.objects.all():
        if uname == i.user1:
            fri.append(i.user2)
            st = str(i.amount1)
            amount.append(st)
            print (amount)
    itmes = friends1.objects.all().filter(user1=request.session['email'])
    # for i in friends1.objects.all():
    #     if uname == i.user1:
    #         x = i.user2
    #         st = i.amount1
    #         friamount.append(x)
    #         friamount.append(st)

    print("add")
    print(itmes)
    # print(friamount)
    return render(request, 'home/friendsadd.html',{'itmes':itmes })


def friexe(request):
    fname = request.POST.get('fname','')
    request.session['fri']=fname
    print(request.session['email'])
    print(request.session['fri'])
    itmes = friendexpense.objects.all().order_by('exp_fri_datetime').reverse().filter(receiver_user=request.session['fri']).filter(payyer_user=request.session['email'])
    return render(request, "home/friexe.html",{'fname':fname ,'itmes':itmes})

def addexp(request):
    uname = request.session['email']
    amo = request.POST.get('amount','')
    type = request.POST.get('add','')
    payoption = request.POST.get('add1','')
    details = request.POST.get('details','')
    fname  =request.session['fri']
    tran_id= friendexpense.objects.latest('id')
    tran_id=tran_id.id+1
    # tran_id=00
    print(tran_id)
    s = friendexpense(adder_user=uname,payyer_user=uname,receiver_user = fname,details=details,amount=amo,exptype=type,details2=payoption,tran_id=tran_id)
    s.save()
    if payoption=='You owe full Expense':
        pay='They owe full Expense'
        s = friendexpense(adder_user=uname, payyer_user=fname, receiver_user=uname, details=details, amount=amo,
                          exptype=type, details2=pay,tran_id=tran_id)
        s.save()
    elif payoption=='They owe full Expense':
        pay='You owe full Expense'
        s = friendexpense(adder_user=uname, payyer_user=fname, receiver_user=uname, details=details, amount=amo,
                              exptype=type, details2=pay,tran_id=tran_id)
        s.save()
    else :
        pay='Split'
        s = friendexpense(adder_user=uname, payyer_user=fname, receiver_user=uname, details=details, amount=amo,
                          exptype=type, details2=pay,tran_id=tran_id)
        s.save()
    for i in friends1.objects.all():
        if i.user1 == uname:
            if i.user2 == fname:
                a = i.amount1
        if i.user1 == fname:
            if i.user2 == uname:
                b = i.amount1

    print(amo)
    s1=0
    s2=0
    if payoption == "Split":
        s1 = a + float(amo) / 2
        s2 = b - float(amo) / 2
    if payoption == "You owe full Expense":
        s1 = a - float(amo)
        s2 = b + float(amo)
    if payoption == "They owe full Expense":
        s1 = a + float(amo)
        s2 = b - float(amo)

    friends1.objects.filter(user1 = uname,user2=fname).update(amount1 = s1)
    friends1.objects.filter(user1 = fname,user2=uname).update(amount1 = s2)
    fri = []
    amount = []
    for i in friends1.objects.all():
        if uname == i.user1:
            fri.append(i.user2)
            st = str(i.amount1)
            amount.append(st)
            print(amount)
    itmes = friends1.objects.all().filter(user1=request.session['email'])
    return render(request,"home/friendsadd.html",{'itmes':itmes })



def friexeupdate(request):

    # fname = request.POST.get('fname','')
    # request.session['fri']=fname
    # print(fname)
    # print(request.session['fri'])
    # itmes = friendexpense.objects.all().order_by('exp_fri_datetime').reverse().filter(receiver_user=request.session['fri']).filter(payyer_user=request.session['email'])
    exeupdate1 = request.POST.get('exeupdate','')

    exeupdate = friendexpense.objects.get(id=exeupdate1)
    print(exeupdate)
    return render(request, "home/friexeupdate.html",{'exeupdate':exeupdate})


def exeup(request):
    exeupdate1 = request.POST.get('exeupdate', '')
    exeupdate = friendexpense.objects.get(id=exeupdate1)

    print(exeupdate)
    uname = exeupdate.payyer_user
    fname = exeupdate.receiver_user
    amo = exeupdate.amount
    for i in friends1.objects.all():
        if i.user1 == uname:
            if i.user2 == fname:
                a = i.amount1
        if i.user1 == fname:
            if i.user2 == uname:
                b = i.amount1

    print(amo)
    s1 = 0
    s2 = 0
    if exeupdate.details2 == "Split":
        s1 = a - float(amo) / 2
        s2 = b + float(amo) / 2
    if exeupdate.details2 == "You owe full Expense":
        s1 = a + float(amo)
        s2 = b - float(amo)
    if exeupdate.details2 == "They owe full Expense":
        s1 = a - float(amo)
        s2 = b + float(amo)

    friends1.objects.filter(user1=uname, user2=fname).update(amount1=s1)
    friends1.objects.filter(user1=fname, user2=uname).update(amount1=s2)
    amo = request.POST.get('amount','')
    type = request.POST.get('add','')
    payoption = request.POST.get('add1','')
    details = request.POST.get('details','')
    for i in friends1.objects.all():
        if i.user1 == uname:
            if i.user2 == fname:
                a = i.amount1
        if i.user1 == fname:
            if i.user2 == uname:
                b = i.amount1

    print(amo)
    s1=0
    s2=0
    exeupdate1 = exeupdate.tran_id
    if payoption == "Split":
        s1 = a + float(amo) / 2
        s2 = b - float(amo) / 2
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.payyer_user).filter(receiver_user=exeupdate.receiver_user).update(details=details, amount=amo, details2=payoption,
                                                                   exptype=type)
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.receiver_user).filter(receiver_user=exeupdate.payyer_user).update(details=details, amount=amo, details2=payoption,
                                                                   exptype=type)

    if payoption == "You owe full Expense":
        s1 = a - float(amo)
        s2 = b + float(amo)
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.payyer_user).filter(
            receiver_user=exeupdate.receiver_user).update(details=details, amount=amo, details2=payoption,
                                                          exptype=type)
        payoption = "They owe full Expense"
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.receiver_user).filter(
            receiver_user=exeupdate.payyer_user).update(details=details, amount=amo, details2=payoption,
                                                        exptype=type)
    if payoption == "They owe full Expense":
        s1 = a + float(amo)
        s2 = b - float(amo)
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.payyer_user).filter(
            receiver_user=exeupdate.receiver_user).update(details=details, amount=amo, details2=payoption,
                                                          exptype=type)
        payoption = "You owe full Expense"
        friendexpense.objects.filter(tran_id=exeupdate1).filter(payyer_user=exeupdate.receiver_user).filter(
            receiver_user=exeupdate.payyer_user).update(details=details, amount=amo, details2=payoption,
                                                        exptype=type)

    friends1.objects.filter(user1 = uname,user2=fname).update(amount1 = s1)
    friends1.objects.filter(user1 = fname,user2=uname).update(amount1 = s2)

    fri = []
    amount = []
    for i in friends1.objects.all():
        if uname == i.user1:
            fri.append(i.user2)
            st = str(i.amount1)
            amount.append(st)
            print(amount)
    itmes = friends1.objects.all().filter(user1=request.session['email'])

    return render(request, "home/friendsadd.html", {'itmes': itmes})

def exedel(request):
    exeupdate1 = request.POST.get('exeupdate','')
    exeupdate = friendexpense.objects.get(id=exeupdate1)
    exeupdate1 = exeupdate.tran_id
    exeupdate =  friendexpense.objects.filter(tran_id=exeupdate1)[0]
    print(exeupdate)
    tran_id=exeupdate.tran_id
    uname=exeupdate.payyer_user
    fname=exeupdate.receiver_user
    print(uname)
    print(fname)
    amo=exeupdate.amount
    for i in friends1.objects.all():
        if i.user1 == uname:
            if i.user2 == fname:
                print(i.amount1)
                a = i.amount1
                print("Aa")
                print(a)
        if i.user1 == fname:
            if i.user2 == uname:
                b = i.amount1
                print("Aa")
                print(b)

    print(amo)
    s1 = 0
    s2 = 0
    print("Aa")
    print(a)
    if exeupdate.details2 == "Split":
        s1 = a - float(amo) / 2
        s2 = b + float(amo) / 2
    if exeupdate.details2== "You owe full Expense":
        s1 = a + float(amo)
        s2 = b - float(amo)
    if exeupdate.details2 == "They owe full Expense":
        s1 = a - float(amo)
        s2 = b + float(amo)

    friends1.objects.filter(user1=uname, user2=fname).update(amount1=s1)
    friends1.objects.filter(user1=fname, user2=uname).update(amount1=s2)
    fri = []
    amount = []
    for i in friends1.objects.all():
        if uname == i.user1:
            fri.append(i.user2)
            st = str(i.amount1)
            amount.append(st)
            print(amount)
    itmes = friends1.objects.all().filter(user1=request.session['email'])
    friendexpense.objects.all().filter(tran_id=tran_id).delete()
    # friendexpense.objects.get(tran_id=tran_id).delete()
    return render(request, "home/friendsadd.html", {'itmes': itmes})
