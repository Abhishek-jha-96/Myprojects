
from django.contrib import admin
from django.urls import path
from posts.views import homepage, post, about, search, category_post_list, allposts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('postlist/<slug>/', category_post_list, name='postlist'),
    path('posts/', allposts, name='allposts'),
    path('search/', search, name='search'),
]
