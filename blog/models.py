from django.db import models
from datetime import datetime

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    #another option for pic uploads
    #image = models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
