from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={
        'placeholder': '*Full Name..',
        #'class': 'form-control'
    }))

    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={
        'placeholder': '*Email..',
        #'class': 'form-control'
    }))

    phone = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={
        'placeholder': '*Contact Number..',
        #'class': 'form-control'
    }))

    message = forms.CharField(max_length=1000, required=True,widget=forms.Textarea(attrs={
        'placeholder': '*Message..',
        'rows': 6,
        #'class': 'form-control'
    }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)