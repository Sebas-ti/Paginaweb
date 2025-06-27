from django.db import models

# Create your models here.

class proyect(models.Model):
    name = models.CharField(max_length=200)
    
class products(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    proyect=models.ForeignKey(proyect,on_delete=models.CASCADE)
    