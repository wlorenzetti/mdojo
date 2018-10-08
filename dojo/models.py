from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Dojo(models.Model):
    """
    Main dojo model
    """

    name = models.CharField(_('Dojo name'), max_length=400)
    address = models.CharField(_('Address'), max_length=400, null=True, blank=True)
    number = models.CharField(_('Number'), max_length=10, null=True, blank=True)
    postal_code = models.IntegerField(_('Postal code'), null=True, blank=True)
    city = models.CharField(_('City'), max_length=255, null=True, blank=True)

    open_date = models.DateField(_('Open date'))

    def __str__(self):
        return self.name


class Deshi(models.Model):

    name = models.CharField(_('Name'), max_length=255)
    surname = models.CharField(_('Surname'), max_length=255)

    birth_day = models.DateField(_('Birth day'), null=True, blank=True)

    tel = models.CharField(_('Phone number'), max_length=255, null=True, blank=True)
    mobile = models.CharField(_('Mobile number'), max_length=255, null=True, blank=True)

    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Levels(models.Model):
    """
    Deshi level: MuKyu, 1° Kyu, ecc
    """
    level = models.CharField(_('Level'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)

    def __str__(self):
        return self.level


class Shiken(models.Model):
    """
    Deshi's exams
    """
    deshi = models.ForeignKey(Deshi, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    date = models.DateField(_('Date'))
    place = models.CharField(_('Place'), max_length=255)




