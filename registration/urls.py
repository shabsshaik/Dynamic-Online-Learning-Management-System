"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Website,name='Website'),
    path('signup',views.SignUpPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('home/payment_free/<str:c_name>',views.payment_free,name='payment_free'),
    path('my_course/',views.mycourse,name='my_course'),
    path('home/payment_free/update/<str:alt>', views.update, name='update'),
    path('course/',views.course,name='course'),
    path('my_course/course_view/<str:c_name>',views.course_view,name='course_view'),
    path('recome/',views.recome,name='recome'),
    path('recome/payment_free/<str:c_name>',views.payment_free,name='payment_free'),
    path('recome/payment_free/update/<str:alt>', views.update, name='update'),
    path('assment/',views.assment,name='assment'),
    path('assment/starttest/<str:c_name>',views.starttest,name='starttest'),
    path('logout/',views.logout,name='recome'),
]
