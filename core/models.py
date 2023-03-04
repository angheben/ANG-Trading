from django.db import models
from stdimage.models import StdImageField


class Employee(models.Model):
    name = models.CharField(name="Name", max_length=100)
    role = models.CharField('core.Role', name='Role', max_length=100)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField(name='Image', upload_to='team', variations={"thumb": {"width": 480, 'height': 480,
                                                                                'crop': True}}, default="N/A")
    facebook = models.CharField("Facebook", max_length=100, default='#')
    twitter = models.CharField("Twitter", max_length=100, default='#')
    instagram = models.CharField("Instagram", max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Testimonial(models.Model):
    pass


class Features(models.Model):
    pass


class Service(models.Model):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
        ('lni-linkedin', 'Linkedin'),
        ('lni-car', 'Car'),
        ('lni-chevron-left', 'Left Arrow'),
        ('lni-chevron-right', 'Right Arrow'),
        ('lni-chrome', 'Chrome'),
        ('lni-comments', 'Comments'),
        ('lni-check-box', 'Slá'),
        ('lni-list', 'Document'),
        ('lni-map', 'Map'),
        ('lni-move', 'Move'),
        ('lni-package', 'Package')
    )
    service = models.CharField(name='Service', max_length=100)
    description = models.TextField(name='Description', max_length=100)
    choices = models.CharField(name='Icon', max_length=100, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
