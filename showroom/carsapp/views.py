from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Showroom, Cars

def index(request):
    cars_list = Cars.objects.order_by('-ratings')
    showroom_list = Showroom.objects.all()
    results = {'cars_list': cars_list, 'showroom_list': showroom_list}
    # print(results)
    return render(request, 'carsapp/index.html', results)

def detail(request, car_id):
    try:
        car = Cars.objects.get(pk=car_id)
        showroom = Showroom.objects.get(pk=car.showroom_id)
        # showroom_count = Cars.objects.filter(showroom_id = showroom.id)
    except:
        raise Http404('Car does not exist in the application')

    return render(request, 'carsapp/detail.html', {'car': car, 'showroom': showroom})

def searchcar(request):
    car_name = request.POST.get('car_name')
    try:
        car = Cars.objects.get(car_name=car_name)
        showroom = Showroom.objects.get(pk=car.showroom_id)
    except (KeyError, Cars.DoesNotExist):
        raise Http404('Car does not exist in the application')

    return render(request, 'carsapp/searchcar.html', {'car': car, 'showroom': showroom})

def searchsr(request):
    sr_name = request.POST.get('sr_name')
    try:
        showroom = Showroom.objects.get(showroom_name=sr_name)
        cars = Cars.objects.filter(showroom=showroom.id)
        # print("showroom--", showroom)
        # print("cars--", cars)
    except (KeyError, Showroom.DoesNotExist):
        raise Http404('Showroom does not exist in the application')  

    return render(request, 'carsapp/searchsr.html', {'cars': cars, 'showroom': showroom})
    