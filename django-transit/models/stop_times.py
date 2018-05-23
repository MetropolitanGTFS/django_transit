from django.db import models
from django.db.models import ForeignKey, CharField, PositiveIntegerField, IntegerField

PICKUP_TYPE_FIELD = (
    (0, 'Regularly scheduled pickup'),
    (1, "No pickup available"),
    (2, "Must phone agency to arrange pickup"),
    (3, "Must coordinate with driver to arrange pickup"),
)

DROP_OFF_TYPE_FIELD = (
    (0, "Regularly scheduled drop off"),
    (1, "No drop off available"),
    (2, "Must phone agency to arrange drop off"),
    (3, "Must coordinate with driver to arrange drop off"),
)

TIMEPOINT_FIELD = (
    (0, "Times are considered approximate"),
    (1, "Times are considered exact"),
)


class Stop_Time(models.Model):
    trip_id = CharField(max_length=100, primary_key=True)
    arrival_time = CharField(max_lenght=8)
    departure_time = CharField(max_lenght=8)
    stop_id = ForeignKey('Stop', related_name='stop_time',
                         on_delete=models.CASCADE)
    stop_sequence = PositiveIntegerField()
    stop_headsign = CharField(max_lenght=300, blank=True, null=True)
    pickup_type = IntegerField(
        choices=PICKUP_TYPE_FIELD,
        default=0,
    )
    drop_off_type = IntegerField(
        choices=DROP_OFF_TYPE_FIELD,
        default=0,
    )
    shape_dist_traveled = CharField(max_lenght=200)
    timepoint = IntegerField(choices=TIMEPOINT_FIELD, default=1)
