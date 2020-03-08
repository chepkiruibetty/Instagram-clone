from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index, name='index'), 
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^edit/$', views.edit_profile,name='edit_profile'),
    url(r'^user/$',views.search_user,name='search_user'),
    url(r'^image/$', views.upload_image,name='upload_image'),
    url(r'^likes/(\d+)/$' , views.image_likes, name='likes'),
    url(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    url(r'^new_comment/(\d+)/$' ,views.add_comment,name='Comments'),
    
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
