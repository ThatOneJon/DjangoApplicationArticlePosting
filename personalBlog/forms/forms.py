from django import forms
from django.contrib.auth.forms import UserCreationForm



class register_Form(UserCreationForm):
    email = forms.CharField(strip=True, max_length=200)


class new_Article(forms.Form):

    headline=forms.CharField(label=False)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 50}), label=False)