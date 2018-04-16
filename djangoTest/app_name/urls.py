from django.conf.urls import url
from app_name import views
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^indexmf/', views.indexMF),
    url(r'^user_list/', views.user_list),
    url(r'^edit-(\d+)/', views.user_edit),
    url(r'^kind/', views.kind),
    url(r'^kindpost/', views.kindpost),
    url(r'^upload_img/', views.upload_img),




]