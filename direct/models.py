from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import date
User = get_user_model()

class Review(models.Model):
    rate_of=models.SmallIntegerField()
    content=models.TextField(blank=True)
    published_at=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return "rate: " + str(self.rate_of) + ", author: " + self.author.username
    def get_author(self):
        return self.author.username
    def save(self, *args, **kwargs):
        print("Saving review:", self.content)
        super().save(*args, **kwargs)
    class Meta:
        ordering=['-published_at']

class Room(models.Model):
    name = models.CharField(max_length=9)
    number = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()

    capacity = models.IntegerField()
    photo=models.ImageField(upload_to="static/images/rooms")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", " + str(self.number)
    class Meta:
        ordering=['-price']
    
class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def everyday_check():
        reservations = Reservation.objects.all()
        for reservation in reservations:
            if reservation.check_out.day < date.today().day:
                reservation.delete()
    
    def __str__(self):
        if self.guest.first_name and self.guest.last_name:
            return f'{self.guest.first_name + " " + self.guest.last_name}; {self.room.name}, {self.room.number}; ({self.check_in} - {self.check_out})'
        else:
            return f'{self.guest.username}; {self.room.name} {self.room.number}; ({self.check_in} - {self.check_out})'