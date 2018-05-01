from django.db import models
from django.db.models import CharField, DecimalField, URLField, ForeignKey, IntegerField, PositiveIntegerField
from . import Agency

ROUTE_TYPE_FIELD = {
    (0, "Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area"),
    (1, "Subway, Metro. Any underground rail system within a metropolitan area"),
    (2, "Rail. Used for intercity or long-distance travel"),
    (3, "Bus. Used for short- and long-distance bus routes"),
    (4, "Ferry. Used for short- and long-distance boat service"),
    (5, "Cable car. Used for street-level cable cars where the cable runs beneath the car"),
    (6, "Gondola, Suspended cable car. Typically used for aerial cable cars where the car is suspended from the cable"),
    (7, "Funicular. Any rail system designed for steep inclines"),
}


class Route(models.Models):
    route_id = IntegerField(primary_key=True)
    agency_id = ForeignKeyField(Agency, on_delete=models.CASCADE)
    route_short_name = CharField(max_length=200)
    route_long_name = CharField(max_length=400)
    route_desc = CharField(max_length=400, blank=True, null=True)
    route_type = IntegerField(choices=ROUTE_TYPE_FIELD)
    route_url = URLField(blank=True, null=True)
    route_color = CharField(max_length=6, min_length=6, default="FFFFFF")
    route_text_color = CharField(max_length=6, min_length=6, default="000000")
    route_sort_order = PositiveIntegerField(blank=True, null=True)

    def __lt__(self, other):
        # self < other
        return self.route_sort_order > other.route_sort_order
