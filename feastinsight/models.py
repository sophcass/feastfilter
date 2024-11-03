from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    formatted_address = models.TextField()
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    type_displayname = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)


class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    text = models.TextField()
    publish_time = models.DateTimeField()
