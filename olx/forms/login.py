from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 15,
        required=True,
        widget =forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'})
    )

    password = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '})
    )
