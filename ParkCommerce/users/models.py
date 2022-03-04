from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, default='profiles/default.jpg')
    social_github = models.CharField(max_length=100, null=True, blank=True)
    social_youtube = models.CharField(max_length=100, null=True, blank=True)
    social_website = models.CharField(max_length=100, null=True, blank=True)
    social_linkedin = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.username or ''
    class Meta:
        ordering = ['name']

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)  
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name or ''

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    body = models.TextField(max_length=500, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.subject or ''
    
    class Meta:
        ordering = ['is_read', '-created']
