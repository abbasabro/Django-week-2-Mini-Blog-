import string
from django import forms
from .models import Post

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Your Password")

class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Your Password")
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        if password:
            if ((len(password) <=8)
            or not any(char.islower() for char in password)
            or not any(char.isupper() for char in password)
            or not any(char.isdigit() for char in password)
            or not any(char in string.punctuation for char in password)
            or ' ' in password
            ):
                self.add_error("password","Your password should be atleast 8 characters long and must contain a Uppercase letter , sybmols")


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'content' , 'img')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'img' : forms.FileInput(attrs={'class':'form-control'})
        }

