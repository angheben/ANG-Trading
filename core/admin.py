from django.contrib import admin
from .models import Service, Features, Testimonial, Employee


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('Service', 'Description', 'Icon')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("Name", "Role", "Image")
