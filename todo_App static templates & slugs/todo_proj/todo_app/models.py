from django.db import models
from django.utils.text import slugify

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    note = models.TextField(blank=False, null=False, default='')
    is_complete = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

 # editing slug using djago shell to existing data in the database using the Django shell 
 #    
# # Open Django shell
# python manage.py shell

# # Import models and utilities
# from Task.models import Task  
# from django.utils.text import slugify

# # Option 1: Fill slugs with titles
# tasks_with_null_slugs = Task.objects.filter(slug__isnull=True)
# for task in tasks_with_null_slugs:
#     task.slug = slugify(task.title)
#     task.save()

# # Option 2: Delete tasks with null slugs
# Task.objects.filter(slug__isnull=True).delete()


