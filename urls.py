from board import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<board_id>\d+)/$', views.show, name='show'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<board_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<board_id>\d+)/update/$', views.update, name='update'),
    url(r'^(?P<board_id>\d+)/delete/$', views.delete, name='delete'),

    url(r'^(?P<board_id>\d+)/comments/$', views.comment_create, name='comment_create'),
    url(r'^(?P<board_id>\d+)/comments/(?P<comment_id>\d+)/delete/$',views.comment_delete,name='comment_delete'),
]
