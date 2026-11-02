from django.urls import path
from . import views
from .views import signup, login_view, logout_view

urlpatterns = [
    path('', views.region_list, name='region_list'),
    path('base',views.base,name="base"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('region/<int:region_id>/', views.soil_list, name='soil_list'),
    path('soil/<int:soil_id>/', views.crop_list, name='crop_list'),
    path('crop/<int:crop_id>/', views.crop_detail, name='crop_detail'),
    path('signup',views.signup,name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
