from django.db import models


class Item(models.Model):
    icon = models.ImageField(upload_to='item_icons/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
