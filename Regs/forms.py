from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CreateUser,self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Enter Email address','id':'exampleInputEmail','aria-describedby':'emailHelp'})
        self.fields['username'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Username','id':'exampleFirstName'})
        self.fields['password1'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Password','id':'examplePasswordInput'})
        self.fields['password2'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Password(repeat)','id':'exampleRepeatPasswordInput'})

class LoginUser(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','email'] 
    def __init__(self, *args, **kwargs):
        super(LoginUser,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Username','id':'exampleFirstName'})
        self.fields['password'].widget.attrs.update({'class':' form-control , form-control-user , form-group , row ','placeholder':'Password','id':'examplePasswordInput'})
              