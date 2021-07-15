from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm, CarForm

# Create your views here.

def brands_list(request):
    brands = Brand.objects.all()
    return render(request, 'cars_and_brands/brands_list.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'cars_and_brands/brand_detail.html', {'brand': brand})

def new_brand(request,):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand.id)
    else:
        form = BrandForm()
    return render(request, 'new_brand.html', {'form': form, 'type_of_request': 'New'})

def edit_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'new_brand.html', {'form': form, 'type_of_request': 'Edit'})

def delete_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand.delete()
    return redirect('brands_list')

# cars

def cars_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = brand.cars.all()
    return render(request, 'cars_and_brands/cars_list.html', {'brand': brand, 'cars': cars, 'type_of_request': 'Cars'})

def car_detail(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    return render(request, 'cars_and_brands/car_detail.html', {'brand': brand, 'car': car})

def new_car(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', car_id=car.id, brand_id=brand.id)
    else:
        form = CarForm()
    return render(request, 'new_car.html', {'form': form, 'type_of_request': 'New'})

def edit_car(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', brand_id=brand.id, car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'new_car.html', {'form': form, 'type_of_request': 'Edit'})

def delete_car(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('brand_detail', brand_id=brand.id)