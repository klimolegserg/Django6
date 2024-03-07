from django.http import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})


def car_details_view(request, car_id):
    car = Car.objects.get(id=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sale = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        return render(request, template_name, {'sales': sale, 'car': car})
    except ObjectDoesNotExist:
        raise Http404('Car not found')
