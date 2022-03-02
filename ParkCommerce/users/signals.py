from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username,
                               email=instance.email, name=instance.first_name)


@receiver(post_delete, sender=Profile)
def deleteUserProfile(sender, instance, *args, **kwargs):
    instance.user.delete()

@receiver(post_save, sender=Profile)
def updateUserProfile(sender, instance, created, *args, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name
        user.save()

