from django import forms
  


class RegForm(forms.Form):
    username=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    e_mail=forms.EmailField(required=False, label='E-mail')
    password=forms.CharField(widget=forms.PasswordInput())
    r_password=forms.CharField(label='Repeat password:', widget=forms.PasswordInput())

