from django.contrib.gis.db import models

class TourConfig(models.Model):
    tour_name = models.CharField(max_length=256)
    tour_logo = models.URLField(verbose_name='URL of tour logo')
    tour_id = models.SlugField(max_length=64, unique=True, db_index=True)
    tour_organization = models.CharField(max_length=256)
    dcs_url = models.URLField(verbose_name='URL of DCS')
    gcm_sender_id = models.CharField(max_length=64)
    start_time = models.PositiveIntegerField()
    max_tour_time = models.PositiveIntegerField()
    is_cancelled = models.BooleanField(default=False, verbose_name='Cancel the tour?')
    tour_route = models.ForeignKey('TourRoute', on_delete=models.PROTECT, blank=True, null=True)
    server_polling_rate = models.PositiveIntegerField(verbose_name='Server Polling Rate (sec)', default=600) #Default time is 10 minutes in seconds
    location_polling_rate = models.PositiveIntegerField(verbose_name='Device Location Polling Rate (sec)', default=45) #Default time is 45 sec in seconds
    server_polling_range = models.PositiveIntegerField(verbose_name='Server Polling Range (sec)', default=5)
    class Meta:
        verbose_name = 'tour'

    def __unicode__(self):
        return unicode(self.tour_name)

class TourRoute(models.Model):
    name = models.CharField(max_length=64)
    route = models.MultiLineStringField()

    def __unicode__(self):
        return unicode(self.name)
