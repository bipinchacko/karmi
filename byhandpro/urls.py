"""byhandpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from byhand import views

from byhandpro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.loginpage,name='login'),

    #######
    path('check_email_exist/',views.check_email_exist,name='check_email_exist'),
    path('check_phone_exist/',views.check_phone_exist,name='check_phone_exist'),

    #######

    path('register_as/',views.register_as,name='register_as'),
    path('register_company/',views.register_company,name='register_company'),
    path('register_freelancer/',views.register_freelancer,name='register_freelancer'),
    path('register_professional/',views.register_professional,name='register_professional'),
    path('register_public/',views.register_public,name='register_public'),
    path('register_student/',views.register_student,name='register_student'),

    ###########
    path('userslist/',views.userslist,name='userslist'),
    path('userview/<int:id>/',views.userview,name='userview'),
    path('follow/<int:id>/',views.follow,name='follow'),
    path('unfollow/<int:id>/',views.unfollow,name='unfollow'),

    #####
    path('social/',include("social.urls")),

    path('longprofile/',include("longprofile.urls")),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
