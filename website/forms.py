from django.forms import ModelForm
from website.models import Contact
from captcha.fields import CaptchaField

class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'