from django.db import models
from tinymce import HTMLField
from django.utils import timezone

class Posts(models.Model):
    title = models.CharField(max_length=200)
    #add WYSIWYG editor to body field in admin
    body = HTMLField('Content')
    image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_at', ]

