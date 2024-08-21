from django.db import models
from django.conf import settings
from restaurants.models import RestaurantLocation
from django.urls import reverse

class Item(models.Model):
    # association
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)

    # item stuff
    name = models.CharField(max_length=120)
    content = models.TextField(help_text='Separate each item by comma')
    excludes = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menus-detail' , kwargs = {'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
    	return self.content.split(",")
    def get_excludes(self):
    	return self.excludes.split(",")