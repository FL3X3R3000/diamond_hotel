from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Review, Room, Reservation
from .forms import ReviewForm, ReservationForm
from users.forms import RegisterForm
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from datetime import date, timedelta
from django.utils import timezone

@login_required
def profile(request):
    print(timezone.now())
    reservations = Reservation.objects.filter(guest=request.user)
    return render(request, 'profile.html', {'user': request.user, "reservations":reservations})

def rooms(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        return render(request, 'rooms.html', {'rooms': rooms})
    

@login_required
def book(request, room_id):
    room = Room.objects.get(id=room_id)
    roomid = room.id
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = Room.objects.get(id=room_id)
            reservation.guest = request.user
            reservation.save()
            return redirect('/')
        else:
            return render(request, 'book.html', {'room':room, 'form': form, 'roomid':roomid})
    else:
        form = ReservationForm()
        return render(request, 'book.html', {'room':room, 'form': form, 'roomid':roomid})


#Забыл пароль
# from django.contrib.auth import get_user_model
# print(list(get_user_model().objects.filter(is_superuser=True).values_list('username', 'password')))


@register.filter
def get_range(value):
    return range(value)

def index(request):
    Reservation.everyday_check()
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            print(review.get_author())
            return redirect("/")
        else:
            reviews = Review.objects.all()
            return render(request, "index.html", context={'reviews': reviews, 'form':form})
    if request.method=="GET":
        reviews = Review.objects.all()
        form = ReviewForm()
        return render(request, "index.html", context={'reviews': reviews, 'form':form})
    

