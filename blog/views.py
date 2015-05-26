from django.shortcuts import render_to_response
from content.models import Post
from blog.forms import RegForm, LoginForm
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.models import User

#option_mes - переменная в которой содержаться опционально выводимые сообщия в шаблоне base.html разделе section

#Тестовый кук не удален !!!

#Отображение стартовой страницы
def home_page(request,option_mes='',page=1):
    #Реализация поиска
    if 'search_input' in request.GET and request.GET['search_input']!='':
        if request.GET.get('search_by')=='all':
            posts=Post.objects.filter(Q(author__username__icontains=request.GET['search_input'])| Q(theme__icontains=request.GET['search_input']))
        elif request.GET.get('search_by')=='theme':
            posts=Post.objects.filter(theme__icontains=request.GET['search_input'])
        else:
             posts=Post.objects.filter(author__username__icontains=request.GET['search_input'])
        if len(posts)==0:
            option_mes='There is no result of this search'
        return render_to_response('base.html',{'option_mes':option_mes,'posts':posts},context_instance=RequestContext(request))
    else:
        posts=Post.objects.all()

    #Реализация счетсчика страниц
    page=int(page)
    page_size=5         #Переменная отвечающая за кол-во постов на одной страничке
    max_view_range=len(posts)//page_size if len(posts)%page_size==0 else len(posts)//page_size+1
    if max_view_range<6:
        view_range=(1,max_view_range+1)
    else:
        view_range=(1,6)          #Отражает диапазон счетчика страниц
    if page>view_range[1] or view_range[1]==(page+1) and max_view_range>6:
        view_range=((page-2),(page+3))
        if view_range[1]>max_view_range:
            view_range=(max_view_range-4,max_view_range+1)
    if page>max_view_range:raise Http404
    view_range=range(*view_range)
    posts=posts[((page-1)*page_size):(page*page_size)]

    #Реализация логина
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
    return render_to_response('base.html',{'option_mes':option_mes,'posts':posts,'view_range':view_range,'current_page':page},context_instance=RequestContext(request))


#Обработка формы регистрации
def reg(request):
    reg_form=RegForm()
    if request.method=='POST' and ('reg_form' in request.POST):
        reg_form=RegForm(request.POST, request.FILES)
        if reg_form.is_valid():
            image=request.FILES['avatar']
            reg_form.create_user(image)
            option_mes='Thanks for registration!'
            return HttpResponseRedirect(reverse('home_page'))
    return render_to_response('auth_form.html',{'reg_form':reg_form},context_instance=RequestContext(request))

#Просмотр странички пользователя
def view_user(request,id):
     viewed_user=User.objects.get(id=id)
     viewed_user_posts=Post.objects.filter(author__id=id)
     return render_to_response('profile.html',{'viewed_user':viewed_user,'viewed_user_posts':viewed_user_posts},context_instance=RequestContext(request))
