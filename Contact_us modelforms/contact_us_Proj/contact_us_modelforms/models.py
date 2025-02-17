from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

    # to migrate the model to the database for this   app
    # 
    # ```bash
    # python manage.py makemigrations contact_us_modelforms
    # python manage.py migrate
    # ``` 
