# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Image, Category
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def display_image(request):
    date = dt.date.today()
    return render(request, 'today.html', {"date": date})


def single_photo(request, photo_id):
    photo = Image.objects.get(id=photo_id)
    return render(request, 'image.html', {'photo': photo})


def all_images(request):
    images = Image.get_images()
    return render(request, 'images.html', {"images": images})


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        photos = Image.search_image(search_term)
        print(photos)
        message = f"{search_term}"
        return render(request, 'search_image.html', {"message": message, "photos": photos})

    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search_image.html', {"message": message})


# def search_locations(request):
#     if 'location' in request.GET and request.GET['location']:
#         search_locations = request.GET.get('location')
#         print(search_locations)
#         photos = Image.filter_by_location(search_locations)
#         print(photos)
#         message = f"{search_locations}"
#         print("hello")
#         return render(request, 'search_image.html', {"message": message, "photos": photos})

#     else:
#         message = 'You haven\'t searched for any photos.'
#         return render(request, 'search_image.html', {"message": message})

def search_locations(request, location_string):
    print(location_string)
    photos = Image.filter_by_location(location_string)
    print(photos)
    message = f"{search_locations}"
    print("hello")
    return render(request, 'search_image.html', {"message": message, "photos": photos})
