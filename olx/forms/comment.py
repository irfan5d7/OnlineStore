from django import forms
from django.forms import ModelForm
from olx.models import Comments

class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['id','user','product']
        widgets = {
            'comments' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add comment here'})
        }
