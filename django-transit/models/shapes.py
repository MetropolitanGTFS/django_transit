from django.db import models
from django.db.models import CharField, IntegerField


class Shapes(models.Model):
    shape_id = CharField(max_length=50)
    shape_pt_lat = CharField(max_length=20)
    shape_pt_lon = CharField(max_length=20)
    shape_pt_sequence = IntegerField()
    shape_dist_traveled = IntegerField(blank=True, null=True)
