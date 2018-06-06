from django.db import models
from django.db.models import CharField, URLField, IntegerField, ForeignKey

EXACT_TIMES_FILD = (
    (0, "Frequency-based trips are not exactly scheduled"),
    (1, "Frequency-based trips are exactly scheduled"),
)


class Frequency(models.Model):
    trip_id = ForeignKey("Trip", on_delete=models.CASCADE)
    start_time = CharField(max_length=8)
    end_time = CharField(max_length=8)
    headway_secs = IntegerField()
    exact_times = IntegerField(choise=EXACT_TIMES_FILD, default=0)
