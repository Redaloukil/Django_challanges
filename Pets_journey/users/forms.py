from django import forms

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=200 ,widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Username',
            }))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
            }))

class SignupForm(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Username',
            }))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'First Name',
            }))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Last Name',
            }))
    password = forms.CharField(max_length=32,widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
            }))
    confirm_password = forms.CharField(max_length=32,widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Confirm Password',
            }))


