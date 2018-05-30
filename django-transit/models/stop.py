from django.db import models
from django.db.models import CharField, DecimalField, URLField, IntegerField, ForeignKey

WHEELCHAIR_BOARDING_FIELD = (
    (0, 'No accessibility information for the stop'),
    (1, 'At least some vehicles at this stop can be boarded by a rider in a wheelchair'),
    (2, 'Wheelchair boarding is not possible at this stop'),
)


class Stop(models.Model):
    stop_id = CharField(max_length=20, unique=True, primary_key=True)
    stop_code = CharField(max_length=20, blank=True, null=True)
    stop_name = CharField(max_length=200)
    stop_desc = CharField(max_length=500, blank=True, null=True)
    stop_lat = DecimalField(max_digits=9, decimal_places=6)
    stop_lon = DecimalField(max_digits=9, decimal_places=6)
    zone_id = CharField(max_length=40, blank=True, null=True)
    stop_url = URLField(blank=True, null=True)
    location_type = CharField(max_length=1, blank=True, null=True)
    parent_station = ForeignKey('Stop', on_delete=models.CASCADE, )
    stop_timezone = CharField(max_length=6, blank=True, null=True)
    wheelchair_boarding = IntegerField(
        choices=WHEELCHAIR_BOARDING_FIELD,
        default=0,
    )
