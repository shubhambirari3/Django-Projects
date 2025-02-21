from django.db import models

# Create your models here.


class owner(models.Model):
    name = models.CharField(max_length=100 , blank= False , null= False)
   
class task(models.Model):
    title = models.CharField(max_length=100 , blank= False , null= False)
    note = models.TextField(blank= False , null= False)
   
   
    def __str__(self):
        return self.title                                                                                                                                                                                                                                       
    

