from django import forms
from django.core import validators


def start_with(value):
    if value[0]!='s':
        raise forms.ValidationError("last name must be started from letter 'S'")


# class StudentForm(forms.Form):
#     name=forms.CharField(validators=[validators.MaxLengthValidator(20)]) # built-in validators
#     lname=forms.CharField(validators=[start_with]) # custom validators 
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     rpassword=forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.Form):
    name=forms.CharField()
    lname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)

    
    def clean(self): #clean() overriden to chck matched fields
        cleaned_data=super().clean()
        password=self.cleaned_data['password']
        rpassword=self.cleaned_data['rpassword']
        if rpassword!=password:
            raise forms.ValidationError("password not matched")
           