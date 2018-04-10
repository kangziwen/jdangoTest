from django.conf.urls import url
from app_name import views
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^indexmf/', views.indexMF),


]