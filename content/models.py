from django.db import models

# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to='videos/')
    youtube_link = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.name