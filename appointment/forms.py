from django import forms
from django.forms import ModelForm
from .models import Appointment, Teacher
from captcha.fields import CaptchaField


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentCreationForm(forms.ModelForm):
    captcha = CaptchaField(
        label='Please enter the characters in the image',
        required=False,
        error_messages={'invalid': 'CAPTCHA invalid. Please try again.'}
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        exclude = ('accepted', 'accepted_date')


class YourForm(forms.Form):
    captcha = CaptchaField()
