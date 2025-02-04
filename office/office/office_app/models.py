from django.db import models

# Create your models here.

class office(models.Model):
    name = models.CharField(max_length=255)

    location = models.CharField(max_length=255)

    employees_count = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
