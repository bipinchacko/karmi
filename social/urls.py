from django.conf.urls import url
from django.urls import path
from social import views

urlpatterns = [

    path('post/',views.PostView,name="post"),
    path('index/',views.index,name="index"),
    path('like/<int:id>',views.like,name="like"),
    path('dislike/<int:id>',views.dislike,name="dislike"),
    path('likecount/<int:id>',views.likecount,name="likecount"),
    path('post-detail/<int:id>',views.post_detail,name="post_detail"),
    path('profile/',views.profile,name="profile"),

]