
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




#Админка
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#Главная страничка
urlpatterns+=patterns('blog.views',
                     url(r'^$','home_page',name='home_page'),
                     url(r'^page/(?P<page>\d+)/$','home_page',name='home_page_view'), #URL служит для перелистывания внизу страници
                     url(r'^registration/$','reg'),
                     url(r'^accounts/login/$','home_page'),
                     url(r'^user/(\d+)/$','view_user',name='view_user')
                     )

#Публикация и просмотр, редактирование постов
urlpatterns+=patterns('content.views',
                      url(r'^create_post/$','create_post', name='post_cre'),
                      url(r'^my_posts/$','my_posts',name='my_posts'),
                      url(r'^post/(\d+)/$','post_view',name='post_view'),
                      url(r'^edit_post/(\d+)/$','post_edit', name='edit_post'),
                      url(r'^delete_post/(\d+)/$','del_post',name='delete_post'),
                     )

urlpatterns+=staticfiles_urlpatterns()