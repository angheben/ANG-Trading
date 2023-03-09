from django.db import models
from stdimage.models import StdImageField


class Employee(models.Model):
    name = models.CharField(name="Name", max_length=100)
    role = models.CharField('core.Role', name='Role', max_length=100)
    bio = models.TextField(name='Bio', max_length=200, default="N/A")
    image = StdImageField(name='Image', upload_to='team', variations={"thumb": {"width": 480, 'height': 480,
                                                                                'crop': True}}, default="N/A")

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Testimonial(models.Model):
    company = models.CharField(name='Company', max_length=100, default="N/A")
    description = models.TextField(name='Description', max_length=300, default="N/A")
    logo = StdImageField(name='Logo', upload_to='testimonial', variations={"thumb": {"width": 300, 'height': 300,
                                                                                     'crop': True}}, default="N/A")

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


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
        ('lni-package', 'Package'),
        ('lni-world', 'World')
    )
    service = models.CharField(name='Service', max_length=100)
    description = models.TextField(name='Description', max_length=100)
    choices = models.CharField(name='Icon', max_length=100, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
