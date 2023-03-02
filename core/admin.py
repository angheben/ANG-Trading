from django.contrib import admin
from .models import Services, Features, Testimonial, Employees


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'choices')
