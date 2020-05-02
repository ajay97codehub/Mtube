from django.db import models

# Create your models here.
class Movies(models.Model):
    mtitle = models.TextField(max_length=300)
    murl=models.URLField() 
    mimg= models.URLField()
    mduration =models.CharField(max_length=300)
    mimdb = models.DecimalField(max_digits=4, decimal_places=1)
    mplot = models.TextField()
    mdirectors = models.TextField()
    mactors = models.TextField()
    mgenres = models.TextField()
    mlanguage= models.CharField(max_length=200)

    def __str__(self):
        return self.mtitle