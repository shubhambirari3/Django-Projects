from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
# Create your views here.

class blogM(models.Model):
    title = models.CharField(max_length=100 , null=False , blank=False)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

def save(self, *args, **kwargs):
    self.slug = generate_slug(self.title)
    super(blogM, self).save(*args, **kwargs)