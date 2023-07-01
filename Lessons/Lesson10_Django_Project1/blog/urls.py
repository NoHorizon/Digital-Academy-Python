from django.urls import path

from blog.views import home_view, post_detail_view

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('posts/<int:pk>/', post_detail_view, name='post-detail')
]
