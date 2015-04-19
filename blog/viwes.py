from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.forms import RegForm, LoginForm
from django.contrib.auth.models import User

#option_mes - переменная в которой содержаться опционально выводимые сообщия в шаблоне base.html
#разделе section

#Отображение стартовой страницы
def home_page(request):
    log_form=LoginForm()

    if request.method=='POST' and ('log_form' in request.POST):
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            log_form=LoginForm(request.POST)

            if log_form.is_valid():
                user=log_form.log_in(request)
                if user is None:
                    option_mes='Wrong username or password'
                else:
                    option_mes='You have succesfully log in!'
                return render_to_response('base.html',{'option_mes':option_mes})

    request.session.set_test_cookie()
    return render_to_response('base.html',{'log_form':LoginForm()})

#Обработка формы регистрации
def reg(request):
    reg_form=RegForm()
    if request.method=='POST' and ('reg_form' in request.POST):
        reg_form=RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.create_user()
            option_mes='Thanks for registration!'
            return render_to_response('base.html',{'option_mes':option_mes})
    return render_to_response('auth_form.html',{'reg_form':reg_form,
                                                'log_form':LoginForm()})
