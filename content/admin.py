from django.contrib import admin
from content.models import Post,Comment, UserImage

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display =('theme','author','pub_date')
    ordering = ('pub_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(UserImage)