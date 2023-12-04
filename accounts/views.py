from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('/')
    
    return render(request, 'login.html')

'''
    msg = None
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            # Check if the username is an email address
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
                return redirect('/')
            else:
                msg = messages.error(request, "User not found. Please try again.")
                

        form = AuthenticationForm()
        context = {'form': form, 'msg': msg}
        return render(request, 'accounts/login.html', context)
    '''