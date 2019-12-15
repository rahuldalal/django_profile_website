from django.urls import path
from .views import all_blogs, blog

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog, name='blog'),
]
