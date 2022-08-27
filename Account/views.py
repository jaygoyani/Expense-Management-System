from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from .models import Account
from Group.models import groupmember
from Friend.models import friends1,friendexpense
from django.core.mail import EmailMessage
from twilio.rest import TwilioRestClient
from twilio.rest import Client


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'home/login.html', c)


def verify(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    for i in Account.objects.all():
        if email == i.email and password == i.password:
            request.session['first_name'] = i.first_name
            request.session['email'] = i.email
            return HttpResponseRedirect('/User/')
    else:
        return render(request, 'home/login.html', {'msg': 'Wrong user id or password'})



def create(request):
    try:
        x = request.session['id']
        return render(request, 'home.html', {'msg1': 'You already have an Account !'})
    except KeyError:
        return render(request, 'home/signup.html')

def signup(request):
    try:
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
        phone_number = request.POST.get('phone_number', '')
        for i in Account.objects.all():
            if email == i.email:
                return render(request, 'home/signup.html', {'msg': 'Email is Already Taken'})
        if password != cpassword:
            return render(request, 'home/signup.html', {'msg': 'Your both Passwords are different'})
        else:
            q = Account(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone_number=phone_number,
            )
            q.save()
            # email1 = EmailMessage('Subject', 'Body', to=[email])
            # email1.send()
            s = groupmember(
                user= email,
                groupdetails = " ",
            )
            s.save()
            print("8527")
            print("fg")
            ii=friendexpense.objects.all()
            print(ii.exists())
            if ii.exists()==False:
                print("iff")
                s = friendexpense(adder_user='a', payyer_user='a', receiver_user='a', details='a', amount=0,
                                  exptype='a', details2='a', tran_id=0)
                s.save()

            return render(request, 'home/login.html', {'msg1': 'Your Account is ready!'})
    except ValueError:
        return render(request, 'home/signup.html', {'msg': 'invalid access !'})


def forgot(request):
    c = {}
    c = c.update(csrf(request))
    return render(request, 'home/forgot.html', c)


'''
    account_sid = "ACa4f0d15dce36666d2308113334d407a1"
    auth_token  = "b24c67c428ee871a65be20a5eab69c56"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body="Generated Temp",
        to="+917990443746",
        from_="+15132943350",
        media_url="http://www.example.com/hearts.png"
    )
    print message.sid
'''


def forgott(request):
    print("forgott")
    try:
        c = {}
        c = c.update(csrf(request))
        otp = randint(100000, 999999)
        request.session['detail'] = request.POST.get('forg')
        request.session['otp'] = otp
        try:
            target = Account.objects.get(email=request.session['detail'])

            subject = 'Forgot Password ?'
            message = '\nYour One Time Password is : ' + str(
                otp) + '\nplease verify to change password\n\nThank you for supporting Us\n'
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.session['detail']]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        except Account.DoesNotExist:
            return render(request, 'home/login.html', {'msg': 'Your Email is not registered'})
        return render(request, 'home/forgot2.html', c)
    except ValueError:
        return render(request, 'home/login.html', {'msg': 'Not registered'})

#
# def verify(request):
#     uid = request.POST.get('uid', '')
#     password = request.POST.get('pass', '')
#     for i in User.objects.all():
#         if uid == i.user_id and password == i.password:
#             request.session['name'] = i.user_name
#             request.session['id'] = i.id
#             request.session['uid'] = i.user_id
#             return HttpResponseRedirect('/Home/')
#     else:
#         return render(request, 'login.html', {'msg': 'Wrong user id or password'})
#
#
def change(request):
    otp = request.session['otp']
    if otp == int(request.POST.get('otp')):
        return render(request, 'home/changepass.html')
    else:
        return render(request, 'home/login.html', {'msg': 'Verification Failed!'})


def verifyt(request):
    password = request.POST.get('pass', '')
    cpass = request.POST.get('cpass', '')
    if password != cpass:
        return render(request, 'home/login.html', {'msg': 'Can not change password. Your both Passwords are different'})
    else:
        target = Account.objects.get(email=request.session['detail'])

        target.password = password
        target.save()
        del request.session['detail']
        return render(request, 'home/login.html', {'msg1': 'Password successfully changed. Please login to enjoy shopping'})
