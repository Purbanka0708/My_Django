from django import forms
from .models import MyVarity


class MyVarityForm(forms.Form):
    my_varity=forms.ModelChoiceField(queryset=MyVarity.objects.all(),label="Select my variety")