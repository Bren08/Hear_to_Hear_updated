from django import forms


class LoginForm(forms.Form):
    """" Login form to login user """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)