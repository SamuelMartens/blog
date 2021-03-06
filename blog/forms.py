from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from content.models import UserImage

class RegForm(forms.Form):
    username=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    e_mail=forms.EmailField(required=False, label='E-mail')
    password=forms.CharField(widget=forms.PasswordInput(),max_length=4)
    r_password=forms.CharField(label='Repeat password:',min_length=4, widget=forms.PasswordInput())
    avatar=forms.FileField()

#Проверка идентичности введенных паролей
    def clean_r_password(self):
        password=self.cleaned_data['password']
        r_password=self.cleaned_data['r_password']
        if password!=r_password:
            raise forms.ValidationError('Different passwords')
        return r_password

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already exist')
        return username




    def create_user(self,image):
        cleaned_data=self.clean()
        user=User.objects.create_user(username=cleaned_data['username'],
                                    first_name=cleaned_data['first_name'],
                                    last_name=cleaned_data['last_name'],
                                    password=cleaned_data['password'])
        user.save()
        UserImage.objects.create(user_to=User.objects.get(username=cleaned_data['username']),
                                        image=image,)

        return user



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

    def log_in(self,request):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
        if request.POST.get('remember_me',None)!=None: request.session.set_expiry(432000) #Кука будет храниться 5 дней
        else: request.session.set_expiry(0)
        return user
