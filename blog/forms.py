from django.forms import ModelForm
from blog.models import link

class ContactForm(ModelForm):
    
    class Meta:
        model = link
        fields = '__all__'