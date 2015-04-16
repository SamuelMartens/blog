from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.forms import RegForm
from django.contrib.auth.models import User

#Отображение стартовой страницы
def home_page(request):
    return render_to_response('base.html',)

#Обработка формы регистрации
#WTF!!!!!!!!!!!!!!!!11111111111111111
def reg(request):
    reg_form=RegForm()
    if request.method=='POST':
        reg_form=RegForm(request.POST)
        #if reg_form.is_valid() and reg_form['password']==reg_form['r_password']:
        if reg_form.is_valid():
            reg_form_cd=reg_form.cleaned_data
            if reg_form_cd['password']==reg_form_cd['r_password']:
                user=User.objects.create_user(username=reg_form_cd['username'],
                                         first_name=reg_form_cd['first_name'],
                                         last_name=reg_form_cd['last_name'],
                                         password=reg_form_cd['password'])
                user.save()
                return render_to_response('auth_form.html',{'test':'Ok'})
    return render_to_response('auth_form.html',{'reg_form':reg_form})
