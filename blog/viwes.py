from django.shortcuts import render_to_response
from blog.forms import RegForm, LoginForm
from django.template import RequestContext
from django.contrib import auth

#option_mes - переменная в которой содержаться опционально выводимые сообщия в шаблоне base.html
#разделе section

#Тестовый кук не удален !!!

#Отображение стартовой страницы
def home_page(request):
    option_mes='Hello user!'
    if request.method=='POST' and ('log_form' in request.POST) and request.session.test_cookie_worked():
        log_form=LoginForm(request.POST)
        if log_form.is_valid():
            user=log_form.log_in(request)
            if user is None:
                option_mes='Wrong username or password'
            else:
                option_mes='You have succesfully log in!'
        else:
            option_mes='No cookies allowed'
    if 'log_out_form' in request.GET:
        auth.logout(request)
        option_mes='You have loged out'
    request.session.set_test_cookie()

    return render_to_response('base.html',{'option_mes':option_mes},context_instance=RequestContext(request))


#Обработка формы регистрации
def reg(request):
    reg_form=RegForm()
    if request.method=='POST' and ('reg_form' in request.POST):
        reg_form=RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.create_user()
            option_mes='Thanks for registration!'
            return render_to_response('base.html',{'option_mes':option_mes},context_instance=RequestContext(request))
    return render_to_response('auth_form.html',{'reg_form':reg_form},context_instance=RequestContext(request))
