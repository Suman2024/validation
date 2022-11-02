from django.core import validators
from django import forms

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('we re start with a,its not considered')

def check_for_len(s):
    if len(s) > 5:
        raise forms.ValueError('lenght isues')

class Studentform(forms.Form):
    name=forms.CharField(max_length=100,validators=[validate_for_a,check_for_len])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    email=forms.EmailField(max_length=100)
    reenter=forms.EmailField(max_length=100)
    phnumber=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('6-9/d{9}')])

    def clean(self):
        e=self.changed_data['email']
        r=self.changed_data['reenter']
        if e!=r:
            raise forms.ValidationError('not matched')
    
    def clean_botcatcher(self):
        data=self.changed_data['botcatcher']
        if len(data)>0:
            raise forms.ValidationError('bot')