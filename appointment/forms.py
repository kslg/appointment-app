from django import forms
from django.forms import ModelForm
from .models import Appointment, Teacher 
from captcha.fields import CaptchaField

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentCreationForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        exclude = ('accepted', 'accepted_date',)
