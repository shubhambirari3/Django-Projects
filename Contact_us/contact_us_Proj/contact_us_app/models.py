from django.db import models

# Create your models here.

class contactM(models.Model):
    name = models.CharField(max_length=100 , blank=False , null=False)
    email = models.EmailField(max_length=100 , blank=False , null=False)
    message = models.TextField(max_length=1000 , blank=False , null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message from {self.name}"