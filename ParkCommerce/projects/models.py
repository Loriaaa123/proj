from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    source_link = models.URLField(null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.FloatField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    # owner
    project = models.ForeignKey("Project", on_delete=models.CASCADE) 
    VOTE_TYPE = {
        ('UP', 'UPVOTE'),
        ('DOWN', 'DOWNVOTE'),
    }
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.name
