from django.db import models
from django.db.models import DateField, IntegerField

EXCEPTION_TYPE_FIELD = {
    (2, "Removed for the specified date"),
    (1, "Added for the specified date"),
}

EXCEPTION_TYPE_DICTIONARY = {
    0: "Removed for the specified date",
    2: "Service is available"
}


class CalendarDates(models.Model):
    service_id = IntegerField()
    exception_type = IntegerField(choices=EXCEPTION_TYPE_FIELD)
    date = DateField()
