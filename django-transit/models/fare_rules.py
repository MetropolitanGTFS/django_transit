from django.db import models
from django.db.models import CharField


class FareRules(models.Model):
    fare_id = CharField(max_length=50)
    origin_id = CharField(max_length=40, blank=True, null=True)
    route_id = CharField(max_length=200, blank=True, null=True)
    destination_id = CharField(max_length=40, blank=True, null=True)
    contains_id = CharField(max_length=40, blank=True, null=True)
