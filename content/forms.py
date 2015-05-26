from django.forms import ModelForm, Textarea
from content.models import Post, Comment
from django.contrib.auth.models import User

class PostCreForm(ModelForm):
    class Meta:
        model=Post
        fields=('theme','post_cont')
        widgets={
            'post_cont':Textarea(attrs={'cols':120,'rows':35}),
        }


    def create_post(self,request):
        post=self.save(commit=False)
        post.author= User.objects.get(username=request.user.username)
        post.save()
        return post

    def edit_post(self,id):
        new_post=self.clean()
        Post.objects.filter(id=id).update(theme=new_post['theme'],post_cont=new_post['post_cont'])


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('comm_cont',)
        widgets={
            'comm_cont':Textarea(attrs={'cols':120,'rows':5}),
        }

    def create_comm(self,request,id):
        comment=self.save(commit=False)
        comment.author=User.objects.get(username=request.user.username)
        comment.post_to=Post.objects.get(id=id)
        comment.save()
        post=Post.objects.get(id=id)
        post.comments_num+=1
        post.save()
        return comment

