from django import forms
from django.forms import ModelForm
from .models import Appointment, Teacher
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Date Picker for the Appointment form
class DateInput(forms.DateInput):
    input_type = 'date'


# Appointment form
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


# Admin Signup form
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
