from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Service, Employee, Testimonial


class IndexView(TemplateView):
    """
    This is the class that will serve for the entire Landing Page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        This function will serve as the interactor between my HTML templates and my DataBase
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        context['employee'] = Employee.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        return context
