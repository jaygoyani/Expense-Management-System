from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
import datetime as DT
from django.template.context_processors import csrf
from .models import user_exp,user_exp1
from Account.models import Account
from datetime import datetime,timedelta
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


# Create your views here.
def userexpense(request):
    c={}
    c.update(csrf(request))
    uname = request.session['email']
    amo = []
    deta = []
    date = []
    ty = []
    on=[]

    # for i in user_exp.objects.all():
    #     if uname == i.username:
    #         amo.append(i.exp_amount)
    #         deta.append(i.exp_details)
    #         date.append(i.exp_date)
    #         ty.append(i.exp_type)
    # n = len(amo)
    # print(n)
    # print(amo)
    # print(deta)
    # print(date)
    # print(ty)

    itmes = user_exp.objects.all().order_by('exp_datetime').reverse().filter(username = request.session['email'])
    print(itmes)
    return render(request,'home/userexpense.html',{'itmes':itmes},c)

def userexpensedel(request):
    userexpensedel = request.POST.get('userexpensedel', '')
    user_exp.objects.get(id=userexpensedel).delete()
    itmes = user_exp.objects.all().order_by('exp_datetime').reverse().filter(username=request.session['email'])
    print(itmes)
    return render(request, 'home/userexpense.html', {'itmes': itmes})


def userexpense1(request):
    try:
        desc=request.POST.get('details','')
        amo=request.POST.get('amount','')
        type = request.POST.get('add','')
        uname = request.session['email']
        print(uname)
        s = user_exp(exp_details=desc,exp_amount=amo,exp_type=type,username = uname)
        s.save()

        on = []
        amo= []
        deta = []
        date = []
        ty = []

        # for i in user_exp.objects.all():
        #     if uname == i.username:
        #         amo.append(i.exp_amount)
        #         deta.append(i.exp_details)
        #         date.append(i.exp_date)
        #         ty.append(i.exp_type)
        # n=len(amo)
        itmes = user_exp.objects.all().order_by('exp_datetime').reverse().filter(username=request.session['email'])

        return render(request, 'home/userexpense.html', {'msg': 'Add succesfully !','itmes':itmes})
    except ValueError:
        return render(request, 'home/userexpense.html', {'msg': 'invalid access !','itmes':itmes})



def profile(request):
    c = {}
    c.update(csrf(request))
    i = Account.objects.get(email=request.session['email'])
    return render(request, 'home/profile.html' ,{'i': i,},c)


def update(request):
    i = Account.objects.get(email=request.session['email'])
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    cpassword = request.POST.get('cpassword', '')
    phone_number = request.POST.get('phone_number', '')
    if password != cpassword:
        return render(request, 'home/profile.html', {'i': i,'msg': 'Your both Passwords are different'})
    else:
        obj = Account.objects.get(email=request.session['email'])
        obj.first_name = first_name
        obj.last_name = last_name
        obj.password = password
        obj.phone_number= phone_number
        obj.save()
        i = Account.objects.get(email=request.session['email'])
        request.session['email'] = obj.email
        request.session['first_name'] = obj.first_name
        return render(request, 'home/profile.html', {'i': i, 'msg1': 'Your data has been updated!'})



def chart(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'home/chart.html')

def chart1(request):
    def last_day_of_month(year, month):
        """ Work out the last day of the month """
        last_days = [31, 30, 29, 28, 27]
        for i in last_days:
            try:
                end = datetime(year, month, i)
            except ValueError:
                continue
            else:
                return end.date()
        return None

    now = datetime.now()
    m = now.month
    y = now.year
    lastday_of_month = last_day_of_month(y, m)

    date_today1 = datetime.now()
    firstdate_of_month1 = date_today1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    firstdate_of_month = firstdate_of_month1.date()

    a = datetime(datetime.today().year, 1, 1)
    b = datetime(datetime.today().year, 12, 31)
    firstdate_of_year = a.date()
    lastdate_of_year = b.date()

    dt = datetime.today()
    s = dt - timedelta(days=dt.weekday())
    e = s + timedelta(days=6)
    firstdate_of_week = s.date()
    lastdate_of_week = e.date()

    print(firstdate_of_week)
    print(lastdate_of_week)
    print(firstdate_of_month)
    print(lastday_of_month)
    print(firstdate_of_year)
    print(lastdate_of_year)
    print("asfgh")
    type1 = request.POST.get('type1','')
    if type1 == '0':
        checked0 = "checked"
        ent_amount = 0
        food_amo = 0
        home_amo = 0
        life_amo = 0
        tran_amo = 0
        utilities_amo = 0
        other_amo = 0
        uname = request.session['email']
        today = DT.date.today()
        for i in user_exp.objects.all():
            # xxx=str(i.exp_date)
            if i.username == uname:
                print(today)
                print(i.exp_date)
                if today == i.exp_date:
                    print("yesss")
                    if i.exp_type == 'Entertainment':
                        ent_amount = ent_amount + i.exp_amount
                    elif i.exp_type == 'Food':
                        food_amo = food_amo + i.exp_amount
                    elif i.exp_type == 'Home':
                        home_amo = home_amo + i.exp_amount
                    elif i.exp_type == 'Life':
                        life_amo = life_amo + i.exp_amount
                    elif i.exp_type == 'Transportation':
                        tran_amo = tran_amo + i.exp_amount
                    elif i.exp_type == 'Utilities':
                        utilities_amo = utilities_amo + i.exp_amount
                    else:
                        other_amo = other_amo + i.exp_amount
        total = ent_amount + food_amo + home_amo + life_amo + tran_amo + utilities_amo + other_amo
        if total==0:
            msg="Not Found Expense Select Date Period "
            return render(request, 'home/chart.html', {'msg':msg, 'checked0': checked0})
        ent_per = (ent_amount / total) * 100
        food_per = (food_amo / total) * 100
        home_per = (home_amo / total) * 100
        life_per = (life_amo / total) * 100
        tran_per = (tran_amo / total) * 100
        uti_per = (utilities_amo / total) * 100
        other_per = (other_amo / total) * 100
        onj1 = {'msg2': ent_per, 'msg3': food_per, 'msg4': home_per, 'msg5': life_per, 'msg6': tran_per,
                'msg7': uti_per,
                'msg8': other_per}
        text = get_template('home/mailchart.txt')
        html = get_template('home/mailchart.html')
        data = {'onj': onj1}
        # If Client cant receive html mails, it will receive the text
        # only version.

        # Render the template with the data

        content_txt = text.render(data)
        content_html = html.render(data)
        #
        # email1 =EmailMultiAlternatives('Daily Report',content_txt,'expansesmanager007@gmail.com',[uname])
        # email1.attach_alternative(content_html, "text/html")
        # email1.send()

        return render(request, 'home/chart.html', {'onj': onj1,'checked0':checked0})

    elif type1 == '1':
        checked1 = "checked"
        ent_amount = 0
        food_amo = 0
        home_amo = 0
        life_amo = 0
        tran_amo = 0
        utilities_amo = 0
        other_amo = 0
        uname = request.session['email']
        today = DT.date.today()
        week_ago = today - DT.timedelta(days=7)
        for i in user_exp.objects.all():
            # xxx=str(i.exp_date)
            # dat = today-i.exp_date
            if i.username == uname:
                # print(dat)
                print(i.exp_date)
                # for j in range(week_ago,today):
                if ((i.exp_date)>=firstdate_of_week) & ((i.exp_date)<=lastdate_of_week):
                    print("yesss")
                    if i.exp_type == 'Entertainment':
                        ent_amount = ent_amount + i.exp_amount
                    elif i.exp_type == 'Food':
                        food_amo = food_amo + i.exp_amount
                    elif i.exp_type == 'Home':
                        home_amo = home_amo + i.exp_amount
                    elif i.exp_type == 'Life':
                        life_amo = life_amo + i.exp_amount
                    elif i.exp_type == 'Transportation':
                        tran_amo = tran_amo + i.exp_amount
                    elif i.exp_type == 'Utilities':
                        utilities_amo = utilities_amo + i.exp_amount
                    else:
                        other_amo = other_amo + i.exp_amount
        total = ent_amount + food_amo + home_amo + life_amo + tran_amo + utilities_amo + other_amo
        if total == 0:
            msg = "Not Found Expense Select Date Period "
            return render(request, 'home/chart.html', {'msg': msg, 'checked1': checked1})
        ent_per = (ent_amount / total) * 100
        food_per = (food_amo / total) * 100
        home_per = (home_amo / total) * 100
        life_per = (life_amo / total) * 100
        tran_per = (tran_amo / total) * 100
        uti_per = (utilities_amo / total) * 100
        other_per = (other_amo / total) * 100
        onj1 = {'msg2': ent_per, 'msg3': food_per, 'msg4': home_per, 'msg5': life_per, 'msg6': tran_per,
                'msg7': uti_per,
                'msg8': other_per}

        return render(request, 'home/chart.html', {'onj': onj1, 'checked1': checked1})

    elif type1 == '2':
        checked2 = "checked"
        ent_amount = 0
        food_amo = 0
        home_amo = 0
        life_amo = 0
        tran_amo = 0
        utilities_amo = 0
        other_amo = 0
        uname = request.session['email']
        today = DT.date.today()
        # week_ago = today - DT.timedelta(days=30)
        for i in user_exp.objects.all():
            # xxx=str(i.exp_date)
            # dat = today-i.exp_date
            if i.username == uname:
                # print(dat)
                print(i.exp_date)
                print("last day month")
                print(firstdate_of_month)
                # for j in range(week_ago,today):
                if ((i.exp_date)>=firstdate_of_month) & ((i.exp_date)<=lastday_of_month):
                    print("yesss")
                    if i.exp_type == 'Entertainment':
                        ent_amount = ent_amount + i.exp_amount
                    elif i.exp_type == 'Food':
                        food_amo = food_amo + i.exp_amount
                    elif i.exp_type == 'Home':
                        home_amo = home_amo + i.exp_amount
                    elif i.exp_type == 'Life':
                        life_amo = life_amo + i.exp_amount
                    elif i.exp_type == 'Transportation':
                        tran_amo = tran_amo + i.exp_amount
                    elif i.exp_type == 'Utilities':
                        utilities_amo = utilities_amo + i.exp_amount
                    else:
                        other_amo = other_amo + i.exp_amount
        total = ent_amount + food_amo + home_amo + life_amo + tran_amo + utilities_amo + other_amo
        if total == 0:
            msg = "Not Found Expense Select Date Period "
            return render(request, 'home/chart.html', {'msg': msg, 'checked2': checked2})
        ent_per = (ent_amount / total) * 100
        food_per = (food_amo / total) * 100
        home_per = (home_amo / total) * 100
        life_per = (life_amo / total) * 100
        tran_per = (tran_amo / total) * 100
        uti_per = (utilities_amo / total) * 100
        other_per = (other_amo / total) * 100
        onj1 = {'msg2': ent_per, 'msg3': food_per, 'msg4': home_per, 'msg5': life_per, 'msg6': tran_per,
                'msg7': uti_per,
                'msg8': other_per}

        return render(request, 'home/chart.html', {'onj': onj1, 'checked2': checked2})

    elif type1 == '3':
        checked3 = "checked"
        ent_amount = 0
        food_amo = 0
        home_amo = 0
        life_amo = 0
        tran_amo = 0
        utilities_amo = 0
        other_amo = 0
        uname = request.session['email']
        today = DT.date.today()
        week_ago = today - DT.timedelta(days=365)
        for i in user_exp.objects.all():
            # xxx=str(i.exp_date)
            # dat = today-i.exp_date
            if i.username == uname:
                # print(dat)
                print(i.exp_date)
                # for j in range(week_ago,today):
                if ((i.exp_date)>=firstdate_of_year) & ((i.exp_date)<=lastdate_of_year):
                    print("yesss")
                    if i.exp_type == 'Entertainment':
                        ent_amount = ent_amount + i.exp_amount
                    elif i.exp_type == 'Food':
                        food_amo = food_amo + i.exp_amount
                    elif i.exp_type == 'Home':
                        home_amo = home_amo + i.exp_amount
                    elif i.exp_type == 'Life':
                        life_amo = life_amo + i.exp_amount
                    elif i.exp_type == 'Transportation':
                        tran_amo = tran_amo + i.exp_amount
                    elif i.exp_type == 'Utilities':
                        utilities_amo = utilities_amo + i.exp_amount
                    else:
                        other_amo = other_amo + i.exp_amount
        total = ent_amount + food_amo + home_amo + life_amo + tran_amo + utilities_amo + other_amo
        if total == 0:
            msg = "Not Found Expense Select Date Period "
            return render(request, 'home/chart.html', {'msg': msg, 'checked3': checked3})
        ent_per = (ent_amount / total) * 100
        food_per = (food_amo / total) * 100
        home_per = (home_amo / total) * 100
        life_per = (life_amo / total) * 100
        tran_per = (tran_amo / total) * 100
        uti_per = (utilities_amo / total) * 100
        other_per = (other_amo / total) * 100
        onj1 = {'msg2': ent_per, 'msg3': food_per, 'msg4': home_per, 'msg5': life_per, 'msg6': tran_per,
                'msg7': uti_per,
                'msg8': other_per}

        return render(request, 'home/chart.html', {'onj': onj1, 'checked3': checked3})


    elif type1 == '4':
        checked4 = "checked"
        ent_amount = 0
        food_amo = 0
        home_amo = 0
        life_amo = 0
        tran_amo = 0
        utilities_amo = 0
        other_amo = 0
        uname = request.session['email']
        today = DT.date.today()
        week_ago = today - DT.timedelta(days=365)
        sdate = request.POST.get('sdate', '')
        edate = request.POST.get('edate', '')
        print(edate)
        print("sasas")
        for i in user_exp.objects.all():
            # xxx=str(i.exp_date)
            # dat = today-i.exp_date
            if i.username == uname:
                # print(dat)
                print(i.exp_date)
                # for j in range(week_ago,today):
                if (str(i.exp_date)>=sdate) & (str(i.exp_date)<=edate):
                    print("yesss")
                    if i.exp_type == 'Entertainment':
                        ent_amount = ent_amount + i.exp_amount
                    elif i.exp_type == 'Food':
                        food_amo = food_amo + i.exp_amount
                    elif i.exp_type == 'Home':
                        home_amo = home_amo + i.exp_amount
                    elif i.exp_type == 'Life':
                        life_amo = life_amo + i.exp_amount
                    elif i.exp_type == 'Transportation':
                        tran_amo = tran_amo + i.exp_amount
                    elif i.exp_type == 'Utilities':
                        utilities_amo = utilities_amo + i.exp_amount
                    else:
                        other_amo = other_amo + i.exp_amount
        total = ent_amount + food_amo + home_amo + life_amo + tran_amo + utilities_amo + other_amo
        if total == 0:
            msg = "Not Found Expense Select Date Period "
            return render(request, 'home/chart.html', {'msg': msg, 'checked4': checked4})
        ent_per = (ent_amount / total) * 100
        food_per = (food_amo / total) * 100
        home_per = (home_amo / total) * 100
        life_per = (life_amo / total) * 100
        tran_per = (tran_amo / total) * 100
        uti_per = (utilities_amo / total) * 100
        other_per = (other_amo / total) * 100
        onj1 = {'msg2': ent_per, 'msg3': food_per, 'msg4': home_per, 'msg5': life_per, 'msg6': tran_per,
                'msg7': uti_per,
                'msg8': other_per}

        return render(request, 'home/chart.html', {'onj': onj1, 'checked4': checked4})
