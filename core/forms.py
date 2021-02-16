from allauth.account.forms import SignupForm, LoginForm
from django.core.validators import RegexValidator
from django import forms

class MyCustomSignupForm(SignupForm):
    def __init__(self,*args,**kwargs):
        super(MyCustomSignupForm,self).__init__(*args,**kwargs)

    name = forms.CharField(max_length = 100, label = 'Fullname')
    family = forms.CharField(max_length = 100)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.family = self.cleaned_data['family']
        user.save()
        return user 

