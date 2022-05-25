from audioop import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from .models import Showroom, Cars

def index(request):
    cars_list = Cars.objects.order_by('-ratings')
    showroom_list_sel = Showroom.objects.all()
    cars_list_sel = Cars.objects.all().values("car_name").distinct()
    results = {'cars_list': cars_list, 'cars_list_sel': cars_list_sel, 'showroom_list_sel': showroom_list_sel}
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
        car = Cars.objects.filter(car_name=car_name)
        # print('car---', car)

        values = []
        for i in range(0, car.count()):
            # print('for---', car[i].showroom_id)
            result = Showroom.objects.get(pk=car[i].showroom_id)
            values.append({'showroom_name': result.showroom_name, 'city': result.city, 'car': car[i]})
        # print('showroom---', values)

    except (KeyError, Cars.DoesNotExist):
        raise Http404('Car does not exist in the application')

    return render(request, 'carsapp/searchcar.html', {'values': values})


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
    

def addcar(request):
    showroom = Showroom.objects.all().values('showroom_name').distinct()
    return render(request, 'carsapp/addcar.html', {'showroom': showroom})

def postcar(request):
    showroom = Showroom.objects.all().values('showroom_name').distinct()
    car_name = request.POST.get('car_name')
    price = request.POST.get('price')
    ratings = request.POST.get('ratings')
    brand = request.POST.get('brand')
    year = request.POST.get('year')
    showroom_nm = request.POST.get('showroom')

    try: 
        showroom_check = Showroom.objects.get(showroom_name=showroom_nm)
    except (KeyError, Showroom.DoesNotExist):
        return render(request, 'carsapp/addcar.html', {'showroom': showroom, 'error_msg': 'Showroom does not exist'})
    else:
        car = Cars(car_name=car_name, price=price, ratings=ratings, brand=brand, model_year=year, showroom_id=showroom_check.id)
        car.save()
        return render(request, 'carsapp/addcar.html', {'showroom': showroom, 'error_msg': 'Car added successfully'})
