from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'contact.html')