from django.db import models

# Create your models here.
from byhand.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    caption = models.CharField(max_length=500,null=True)

    date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=1000,null=True)
    image = models.ImageField(upload_to='media',null=True,blank=True)
    likes = models.IntegerField(default = 0)
    comments =models.IntegerField(default = 0)


class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True,related_name="like")

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True,related_name="comment")
    comment = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(auto_now=True)