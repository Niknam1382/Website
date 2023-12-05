from django.forms import ModelForm
from blog.models import link
from blog.models import Comment
from captcha.fields import CaptchaField

class ContactForm(ModelForm):
    class Meta:
        model = link
        fields = '__all__'

class CommentForm(ModelForm) :
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post', 'first_name', 'last_name', 'email',  'message',]