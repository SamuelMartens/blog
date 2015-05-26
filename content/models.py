from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User)
    theme=models.CharField(max_length=60)
    post_cont=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    comments_num=models.PositiveIntegerField(default=0)

    def __str__(self):
        return u'%s , %s' % (self.theme, self.author)

    class Meta:
        ordering=['-pub_date']


class Comment(models.Model):
    post_to=models.ForeignKey(Post)
    author=models.ForeignKey(User)
    comm_cont=models.TextField(max_length=400)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  '%s , %s' % (self.author,self.comm_cont)

    def delete_comment(self,id):
        self.delete()
        post=Post.objects.get(id=id)
        post.comments_num-=1
        post.save()

#class PostImage(models.Model):
    #post_to=models.ForeignKey(Post)
   # pub_date=models.DateField(auto_now_add=True)
    #image_comment=models.CharField(max_length=30)
    #image=models.FileField(upload_to='/post_image/',)

class UserImage(models.Model):
    user_to=models.ForeignKey(User)
    image=models.FileField(upload_to='user_image/')







