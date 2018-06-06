from django.db import models
from django.db.models import CharField, URLField, IntegerField, ForeignKey


class FeedInfo(models.Model):
    feed_publisher_name = CharField(max_length=200)
    feed_publisher_url = URLField()
    feed_lang = CharField(max_length=10)
    feed_start_date = CharField(max_length=8, blank=True, null=True)
    feed_end_date = CharField(max_length=8, blank=True, null=True)
    feed_version = CharField(max_length=40, blank=True, null=True)
