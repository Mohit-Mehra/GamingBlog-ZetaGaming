from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileModel

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
       model = User
       fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
    def __init__(self,*args, **kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for filedname in ['first_name','last_name', 'username', 'email', 'password1' ,'password2']:
            self.fields[filedname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
    
    def __init__(self,*args, **kwargs):
        super(UserUpdateForm,self).__init__(*args,**kwargs)
        for filedname in ['first_name','last_name','username','email']:
            self.fields[filedname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']





