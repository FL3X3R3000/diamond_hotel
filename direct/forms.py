from django import forms
from .models import Review, Reservation, Room
from django.utils import timezone
from datetime import date, timedelta
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rate_of', 'content']
    
    def clean(self):
        cleaned_data = super().clean()
        rate_of = cleaned_data.get('rate_of')
        content = cleaned_data.get('content')

        if rate_of and content:
            if rate_of > 5 or rate_of < 1:
                self.add_error('rate', 'Please, set the rating.')


class ReservationForm(forms.ModelForm):
    roomid = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    YEARS=[timezone.now().year,]
    MONTHS=[timezone.now().month,]
    DAYS=[f'{date.today().day}', f'{(date.today() + timedelta(1)).day}', f'{(date.today() + timedelta(2)).day}', f'{(date.today() + timedelta(3)).day}', f'{(date.today() + timedelta(4)).day}', f'{(date.today() + timedelta(5)).day}']
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out']

    def crossed(self, cin1, cout1, cin2, cout2):
        a = [a for a in range(cin1, cout1+1)]
        print(a)
        b=[b for b in range(cin2, cout2+1)]
        print(b)
        res=[]
        for i in a:
            for j in b:
                if i == j:
                    res.append("False")
        return "False" in res

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['check_in'] = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
        self.fields['check_out'] = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
        print(self.DAYS)
        print(self.YEARS)
        print(self.MONTHS)
    def is_valid_date(self, date):
        return (date.year in self.YEARS and date.month in self.MONTHS and str(date.day) in self.DAYS)
    def clean(self):
        check_in = self.cleaned_data['check_in']
        check_out = self.cleaned_data['check_out']
        room = Room.objects.get(id=self.cleaned_data['roomid'])

        if check_in > check_out:
            self.add_error('check_out', 'Check-out date must be after check-in date.')
            return

        if not self.is_valid_date(check_in) or not self.is_valid_date(check_out):
            return

        conflicting_reservations = Reservation.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_in)

        if conflicting_reservations.exists():
            self.add_error('check_in', 'Sorry, but this date is unavailable now.')



