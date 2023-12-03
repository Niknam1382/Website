from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'home.html')

def aboutus_view(request):
    return render(request, 'about-us.html')

def services_view(request):
    return render(request, 'services.html')

def aboutme_view(request):
    return render(request, 'about-me.html')

def team_view(request):
    return render(request, 'team.html')

def project_view(request):
    return render(request, 'projects.html')

def contact_view(request):
    if request.method == 'POST':
        # next_url = request.POST.get('next')
        # <input type="hidden" name="next" value="{{request.path}}" />
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg = messages.success(request, "پیام شما با موفقیت ثبت شد")
            # return redirect(next_url)
            return redirect('/')
        else:
            msg = messages.warning(request, "ثبت پیام شما با خطا مواجه شد")
            return redirect('/')
        if msg :
            context[str(msg)] = messages.success(request, "پیام شما با موفقیت ثبت شد")

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html',context)