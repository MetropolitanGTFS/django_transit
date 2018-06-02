from django.db import models
from django.db.models import FloatField, CharField, IntegerField, ForeignKey

TRANSFERS_FIELD = {
    (0, "No transfers permitted on this fare"),
    (1, " Passenger may transfer once"),
    (2, "Passenger may transfer twice"),
    (None, "If this field is empty, unlimited transfers are permitted")
}
PAYMENT_METHOD_FIELD = {
    (0, "Fare is paid on board"),
    (1, "Fare must be paid before boarding"),
}


class FareAttributes(models.Model):
    fare_id = CharField(max_length=50)
    price = FloatField()
    currency_type = CharField(max_length=50)
    transfers = IntegerField(choices=TRANSFERS_FIELD)
    payment_method = IntegerField(choices=PAYMENT_METHOD_FIELD)
    agency_id = ForeignKey('Agency', blank=True,
                           null=True, on_delete=models.CASCADE)
    transfer_duration = IntegerField(blank=True, null=True)
