from django.db import models
from datetime import datetime
from tinymce import HTMLField

class Posts(models.Model):
    title = models.CharField(max_length=200)
    #add WYSIWYG editor to body field in admin
    body = HTMLField('Content')
    image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
