from django.db import models
from stdimage.models import StdImageField


class Employees(models.Model):
    pass


class Testimonial(models.Model):
    pass


class Features(models.Model):
    pass


class Services(models.Model):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket')
    )
    service = models.CharField(name='service', max_length=100)
    description = models.CharField(name='description', max_length=100)
    choices = models.CharField(name='choices', max_length=100, choices=ICON_CHOICES)
