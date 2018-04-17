from django.conf.urls import url
from app02 import views
urlpatterns = [
    url(r'^login/',views.login),
    url(r'^upload/', views.upload),
    url(r'^upload_file/', views.upload_file),
    url(r'^app/', views.app),

]