from django import forms


class LoginForm(forms.Form):
    """
    Form to handle login users into the website.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)