from django.contrib import messages
from django.shortcuts import render, redirect

from apps.contents.utils import phone_validation, full_name_validation
from apps.contents.models import Car, Contact, CarImage


def home_page(request):
    cars = Car.objects.filter(status=True)
    if cars.count() >= 4:
        cars = cars[:4]
    else:
        cars = Car.objects.all()[:4]
    return render(request, 'home/home.html', context={'cars': cars})


def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    images = CarImage.objects.filter(car=car)   

    if request.method == 'POST':
        data = {
            'full_name': request.POST.get('full_name'),
            'phone_number': request.POST.get('phone_number'),
            'date_start': request.POST.get('date_start'),
            'date_end': request.POST.get('date_end'),
            'city': car.city,
            'auto': car
        }
        if not data['date_start'] or not data['date_end']:
            messages.error(request, 'Заполните даты')
            return redirect('car_detail', pk=car.pk)
        
        valids = [full_name_validation(full_name=data.get('full_name', None)), 
            phone_validation(phone_number=data.get('phone_number', None))]
        
        for valid in valids:
            if not valid['status']:
                messages.error(request, valid['message'])
                return redirect('car_detail', pk=car.pk)
            
        Contact.objects.create(**data)
        return redirect('home')  
    
    return render(request, 'home/car.html', context={'car': car, 'images': images})


def contact(request):
    return render(request, 'home/contact.html')


def feedbacks(request):
    return render(request, 'home/feedbacks.html')

def terms(request):
    return render(request, 'home/terms.html')

def autopark(request):
    return render(request, 'home/autopark.html', context={'cars': Car.objects.all()})