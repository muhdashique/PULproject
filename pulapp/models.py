from django.db import models

# Create your models here.



class FuelRate(models.Model):
    country = models.CharField(max_length=100)
    fuel_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.country} - {self.fuel_rate}"






class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

