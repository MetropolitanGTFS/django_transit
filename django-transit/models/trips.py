from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey

DIRECTION_ID_FIELD = {
    (0, "Travel in one direction"),
    (1, "Travel in the opposite direction"),
}

WHEELCHAIR_ACCESSIBLE_FIELD = {
    (0, "Indicates that there is no accessibility information for the trip"),
    (
        1,
        "Indicates that the vehicle being used on this particular trip can accommodate at least one rider in a wheelchair",
    ),
    (2, "Indicates that no riders in wheelchairs can be accommodated on this trip"),
}

BIKES_ALLOWED_FIELD = {
    (0, "Indicates that there is no bike information for the trip"),
    (
        1,
        "Indicates that the vehicle being used on this particular trip can accommodate at least one bicycle",
    ),
    (2, "Indicates that no bicycles are allowed on this trip"),
}


class Trip(models.Model):
    route_id = ForeignKey("Route", related_name="route_id", on_delete=models.CASCADE)
    service_id = CharField(max_length=300, unique=True)
    trip_id = CharField(max_length=300, primary_key=True)
    trip_headsign = CharField(max_lengh=300, blank=True, null=True)
    trip_short_name = CharField(max_length=200, blank=True, null=True)
    direction_id = IntegerField(choices=DIRECTION_ID_FIELD, blank=True, null=True)
    block_id = CharField(max_length=50, blank=True, null=True)
    wheelchair_accessible = IntegerField(choices=WHEELCHAIR_ACCESSIBLE_FIELD, default=0)
    bikes_allowed = IntegerField(choices=BIKES_ALLOWED_FIELD, default=0)
