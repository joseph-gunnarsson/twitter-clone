from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Following(models.Model):
    user_id = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers",on_delete=models.CASCADE)
class Avatar(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to="media")
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
