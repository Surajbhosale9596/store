from . import views
from django.urls import path

urlpatterns=[
    path('',views.item),
    # path('signup',views.signup),
    # path('login/',views.login),
    path('accounts/signup',views.signup,name='signup'),
    path('order',views.order),
    path('home',views.item),
    path('home',views.home),
    path('contact',views.contact),
    path('about',views.about)
    ]