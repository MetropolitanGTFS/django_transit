from django.db import models
from django.db.models import CharField, URLField, IntegerField, ForeignKey

TRANSFER_TYPE_FIELD = (
    (0, "This is a recommended transfer point between routes"),
    (1, "This is a timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one, with sufficient time for a passenger to transfer between routes"),
    (2, "This transfer requires a minimum amount of time between arrival and departure to ensure a connection"),
    (3, "Transfers are not possible between routes at this location")
)


class Transfer(models.Model):
    from_stop_id = CharField(max_length=20, unique=True, primary_key=True)
    to_stop_id = CharField(max_length=20, unique=True, primary_key=True)
    Transfer_type = IntegerField(choices=TRANSFER_TYPE_FIELD, default=0)
    min_transfer_time = IntegerField(blank=True, null=True)
