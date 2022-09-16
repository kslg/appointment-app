from django import forms
from django.forms import ModelForm
from .models import Appointment, Teacher 


class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        exclude = ('accepted', 'accepted_date',)