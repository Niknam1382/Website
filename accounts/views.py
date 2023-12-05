from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm
from django.conf import settings
from django.core.mail import EmailMessage , send_mail
import random
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    msg = None
    if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
                email = username
                user = User.objects.filter(email=email).first()
                if user:
                    username = user.username
                user = authenticate(request, username=username, password=password)
            else:
                user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                msg = messages.success(request, 'با موفقیت وارد شدید')
                return redirect('/')
            else:
                msg = messages.error(request, "User not found. Please try again.")
    
    return render(request, 'login.html', {'msg': msg})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    msg = None
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                email = data['email']
                password = data['password']
                first_name = data['first_name']
                last_name = data['last_name']
                confirm = request.POST.get('confirm')
                if not User.objects.filter(email = email) and password == confirm :
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/accounts/login')
                else :
                    msg = messages.warning(request, "ثبت نام با خطا مواجه شد | ممکن است ایمیل یا یوزرنیم تکراری باشد")
                    return render(request, 'signup.html',{'msg':msg})
        form = UserForm()
        return render(request, 'signup.html',{'form':form, 'msg':msg})
    else:
        return redirect('/')
    
def reset_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            Email = request.POST["email"]
            user_email = Email
            Email = [str(Email)]
            l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9]
            key = ''
            for i in range(6):
                key = key + str(random.choice(l))
            key = str(key)
            subject = 'reset password'
            message = 'Your reset password Confirmation Code :  ' + key
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage(subject, message, email_from, tuple(Email))
            email.send()
            send_mail(subject, message, email_from, Email)
            request.session['user_email'] = user_email
            request.session['reset_code'] = key
            return redirect('/accounts/change')
    return render(request, 'reset.html')


def change_password(request):
    msg = None
    if request.method == 'POST':
        password2 = request.POST["password"]
        password2c = request.POST["password2"]
        confirm = request.POST["confirm"]
        if not password2 == password2c:
            msg = messages.warning(request, "اشکال در وارد کردن رمز")
        if password2 == password2c:
            user_email = request.session.get('user_email')
            reset_code = request.session.get('reset_code')
            if str(password2) == str(password2c):
                if confirm == reset_code:
                    try:
                        user = User.objects.get(email=user_email)
                        user.set_password(password2)
                        user.save()
                        msg = messages.success(request, "تغییر رمز با موفقیت انجام شد")
                        return redirect('/accounts/login')
                    except User.DoesNotExist:
                        msg = messages.warning(request, "لطفا دوباره تلاش کنید")
                        return redirect('/accounts/reset-password')
    return render(request, 'change.html', {msg: msg})