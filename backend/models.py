from django.db import models
from django.core.validators import RegexValidator
from PIL import Image

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            new_img = img.resize((450, 350), Image.Resampling.LANCZOS)
            new_img.save(self.image.path)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            new_img = img.resize((450, 350), Image.Resampling.LANCZOS)
            new_img.save(self.image.path)

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17) 
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)