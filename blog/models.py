from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class SensorManagement(models.Model):
    manager = models.ForeignKey('auth.User')
    userId = models.AutoField(primary_key=True)
    nodeId = models.IntegerField(max_length=10,null=False)
    Latitude = models.FloatField(max_length=20)
    Longitude = models.FloatField(max_length=20)
    Address = models.CharField(max_length=100)
    Type = models.CharField(max_length=10)
    img = models.ImageField(upload_to='pic_folder/', default='pic_folder/unknown_icon.png')
