from django.db import models


class Agency(models.Model):
    agency_id = models.CharField(
        max_length=255, blank=True, null=True, unique=True)
    agency_name = models.CharField(max_length=400)
    agency_url = models.URLField()
    agency_timezone = models.CharField(max_length=20)
    agency_lang = models.CharField(max_length=2, null=True, blank=True)
    agency_phone = models.CharField(max_length=20, null=True, blank=True)
    agency_fare_url = models.URLField(null=True, blank=True)
    agency_email = models.EmailField(null=True, blank=True)
