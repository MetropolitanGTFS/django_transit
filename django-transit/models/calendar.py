from django.db import models
from django.db.models import DateField, IntegerField

DAY_FIELD = {
    (0, "Service is not available"),
    (1, "Service is available"),
}

DAY_DICTIONARY = {
    0: "Service is not available",
    1: "Service is available"
}


class Route(models.Model):
    service_id = IntegerField()
    monday = IntegerField(choices=DAY_FIELD)
    tuesday = IntegerField(choices=DAY_FIELD)
    wednesday = IntegerField(choices=DAY_FIELD)
    thursday = IntegerField(choices=DAY_FIELD)
    friday = IntegerField(choices=DAY_FIELD)
    saturday = IntegerField(choices=DAY_FIELD)
    sunday = IntegerField(choices=DAY_FIELD)
    start_date = DateField()
    end_date = DateField()
