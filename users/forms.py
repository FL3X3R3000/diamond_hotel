from django import forms as fm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'date_joined', 'email','password1','password2']
    def is_blank(self):
        stat=False
        for field in self.fields:
            if not field:
                stat=True
        return stat
            
    
class LoginForm(fm.Form):
    username= fm.CharField(max_length=20, label="Enter username", required=True)
    password=fm.CharField(max_length=40, label="Enter password", widget=fm.PasswordInput, required=True)