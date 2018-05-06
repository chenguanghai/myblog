from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^home$',views.HomeView().as_view(),name='home'),# 首页
]