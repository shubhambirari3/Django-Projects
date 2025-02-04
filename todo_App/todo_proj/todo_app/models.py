from django.db import models

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=100 , blank= False , null= False)
    note = models.TextField(blank= False , null= False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title                                                                                                                                                                                                                                       
    

