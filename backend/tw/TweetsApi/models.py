from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    tweetcotent= models.CharField(max_length=200)
    image=models.ImageField(upload_to="../media",default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    retweets=models.IntegerField(default=0)
    commentscount=models.IntegerField(default=0)
    iscomment=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,related_name='tweet',null=True)
    comment=models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comment',null=True)

class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen=models.BooleanField(default=False)
