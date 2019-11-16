from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('<int:post_id>', views.view_post, name='view_post')
]