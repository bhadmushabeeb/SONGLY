from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "music"
urlpatterns = [
    path('@/', views.index, name ='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('music/<int:album_id>/', views.detail, name='detail'),
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    path('', views.ind2, name='rr'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
    path('det/<int:album_id>/', views.det2, name='det'),

    path('<int:pk>/favorite/', views.favorite, name='favorite'),
    re_path(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    re_path(r'^create_album/$', views.create_album, name='create_album'),
    re_path(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
