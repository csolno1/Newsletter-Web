from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label = "inputUsername", max_length=100)
    email = forms.CharField(label = "inputEmail", max_length=100)
    password = forms.CharField(label = "inputPassword", max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label = "inputUser", max_length=100)
    password = forms.CharField(label = "inputPassword", max_length=100)
