from django.contrib import admin
from .models import Service, Testimonial, Employee


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('Service', 'Description', 'Icon')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("Name", "Role", "Image")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("Company", "Description", "Logo")
