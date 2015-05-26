from django.shortcuts import render_to_response
from content.forms import PostCreForm,CommentForm
from content.models import Post, Comment
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

@login_required
def create_post(request):
    post=PostCreForm()
    if request.method=='POST' and ('post_cre_form' in request.POST):
        post=PostCreForm(request.POST)
        if post.is_valid():
            post.create_post(request)
            option_mes='Post has been created'
            return HttpResponseRedirect(reverse('home_page'))
    return render_to_response('post_cre.html',{'post_cre_form':post},context_instance=RequestContext(request))

@login_required
def my_posts(request):
    author_posts=Post.objects.filter(author=request.user.id)
    return render_to_response('my_posts.html',{'author_posts':author_posts,},context_instance=RequestContext(request))

def post_view(request,id):
    comments=Comment.objects.filter(post_to=id)
    comment=CommentForm()
    post=Post.objects.get(id=id)
    if request.method=='POST':
        #Создание коммента
        if 'cre_comm' in request.POST:
            comment=CommentForm(request.POST)
            if comment.is_valid():
                comment.create_comm(request,id)
                return HttpResponseRedirect(reverse('post_view',args=[id,]))
        #Удаление коммента
        if 'delete_comment_id' in request.POST:
            comment_del=Comment.objects.get(id=int(request.POST['delete_comment_id']))
            comment_del.delete_comment(id)
    return render_to_response('post_view.html',{'post':post,'comments':comments,'comment':comment},context_instance=RequestContext(request))

#Функция проверяет является ли тот кто хочет произвести какое-лиоб действие с постом его автором
def check_author(request,id):
    post=Post.objects.get(id=id)
    if str(post.author)!=request.user.username:
        raise Http404()
    return post

@login_required
def post_edit(request,id):
    post=check_author(request,id)
    ed_post=PostCreForm({'theme':post.theme,
                         'post_cont':post.post_cont})
    if request.method=='POST' and ('post_cre_form' in request.POST):
        ed_post=PostCreForm(request.POST)
        if ed_post.is_valid():
            ed_post.edit_post(id)
            return HttpResponseRedirect(reverse('post_view',args=[id,]))
    return render_to_response('post_cre.html',{'post_cre_form':ed_post},context_instance=RequestContext(request))

@login_required
def del_post(request,id):
    post=check_author(request,id)
    if 'yes' in request.GET:
        post.delete()
        return  HttpResponseRedirect(reverse('my_posts'))
    elif 'no' in request.GET:return HttpResponseRedirect(reverse('my_posts'))
    return render_to_response('del_post.html',{'post':post},context_instance=RequestContext(request))
