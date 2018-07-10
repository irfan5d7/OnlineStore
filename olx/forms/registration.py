from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name '})
    )

    last_name = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name '})
    )

    username = forms.CharField(
        max_length = 15,
        required=True,
        widget =forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'})
    )

    email = forms.CharField(
        max_length=32,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
    )

    password = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '})
    )


