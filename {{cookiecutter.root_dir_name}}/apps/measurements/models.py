from django.db import models

class Stations(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(
        "Latitude of station",
        max_digits=9,
        decimal_places=6
    )
    longitude = models.DecimalField(
        "Longitude of station",
        max_digits=9,
        decimal_places=6
    ) 

    def __str__(self):
        return self.name


class Measurements(models.Model):
    station = models.ForeignKey(
        Stations,
        on_delete=models.CASCADE
    )
    class Products(models.TextChoices):
        """ Measured parameter """
        AIR_TEMPERATURE = 'at', 'Air Temperature'
        WATER_TEMPERATURE = 'wt', 'Water Temperature'
        SALINITY = "st", "Salinity"

    product = models.CharField(
        max_length=2,
        choices=Products.choices
    )
    value = models.FloatField()
    