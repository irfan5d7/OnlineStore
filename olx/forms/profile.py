from django import forms
from olx.models import UserProfile


class AddProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id','user']
        widgets = {
            'picture':forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Picture'}),
            'contact_no' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'address' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address'})
        }