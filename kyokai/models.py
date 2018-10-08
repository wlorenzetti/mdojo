from django.db import models
from django.utils.translation import ugettext_lazy as _
from dojo.models import Dojo


class Kyokai(models.Model):
    """
    Those assocations dojos can affiliate.
    """
    name = models.CharField(_('Association(Kyokai) name'), max_length=400)

    address = models.CharField(_('Address'), max_length=400, null=True, blank=True)
    number = models.CharField(_('Number'), max_length=10, null=True, blank=True)
    postal_code = models.IntegerField(_('Postal code'), null=True, blank=True)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)

    website = models.URLField(_('Web site URL'), max_length=1000, null=True, blank=True)

    facebook = models.URLField(_('Web site URL'), max_length=1000, null=True, blank=True)
    twitter = models.URLField(_('Web site URL'), max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Affiliation(models.Model):
    """
    Annual affilations
    """
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    kyokai = models.ForeignKey(Kyokai, on_delete=models.CASCADE)
    start_date = models.DateField(_('Start affiliation'))
    end_date = models.DateField(_('End affiliation'), null=True, blank=True)

    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=7, null=True, blank=True)

    def __str__(self):
        return "{} {}-{}".format(self.kyokai, self.start_date.year, int(self.start_date.year) + 1)

