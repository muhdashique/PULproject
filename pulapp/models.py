from django.db import models

# Create your models here.


from django.db import models

class FuelRate(models.Model):
    country = models.CharField(max_length=100)
    fuel_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.country} - {self.fuel_rate}"






