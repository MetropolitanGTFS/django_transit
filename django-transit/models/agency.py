from django.db import models
from django.db.models import CharField, URLField, EmailField


class Agency(models.Model):
    agency_id = CharField(max_length=255, blank=True, null=True, unique=True)
    agency_name = CharField(max_length=400)
    agency_url = URLField()
    agency_timezone = CharField(max_length=20)
    agency_lang = CharField(max_length=2, null=True, blank=True)
    agency_phone = CharField(max_length=20, null=True, blank=True)
    agency_fare_url = URLField(null=True, blank=True)
    agency_email = EmailField(null=True, blank=True)
