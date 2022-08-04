from django.db import models


# Create your models here.
class Tariff(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return f"{self.title}-{self.price}"

