from django import forms
import django
from django.core import validators


def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('we re start with a,its not considered')

def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('lenght isues')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validate_for_a,check_for_len])
    email=forms.EmailField()
    reenter=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    phnumber=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])



    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('reenter')
        if e!=r:
            raise forms.ValidationError('not matched')
    
    
    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('bot')