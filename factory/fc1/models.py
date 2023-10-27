from django.db import models
from django.urls import reverse

class ConfectioneryFactoryproduct1(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('factory1:product_detail', args=(self.pk, ))
