from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.core.mail import EmailMessage, message, send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate #login_request
from django.contrib.auth.forms import AuthenticationForm #login_request
from .models import Appointment
from .forms import AppointmentCreationForm
from django.template import Context
from django.template.loader import render_to_string, get_template
import datetime
from django.urls import reverse

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

# CREATE APPOINTMENT
def appointment_template_view(request):
        form = AppointmentCreationForm()
        if request.method == 'POST':
            form = AppointmentCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     f"Thanks for making an appointment,\
                                     we will email you soon to confirm.")
                return redirect('appointment')
        return render(request, 'appointment.html', {'form': form})


# MANAGE APPOINTMENT
class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()
        email = appointment.email

        # Send Email
        send_mail(
            'Your appointment confirmed at Fairchild School',
            'Hello, your appointment has been confirmed. See you soon.',
            'krishantest7@gmail.com',
            [email],
            )

        messages.add_message(request, messages.SUCCESS,
                             f"You accepted the appointment\
                             of {appointment.parent_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Manage Appointments"
        })
        return context


# # DELETE APPOINTMENT
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS,
                        f"The appointment has been deleted.")
    return redirect('manage')


# AJAX
def load_classes(request):
    teacher_id = request.GET.get('teacher_id')


# LOGIN PAGE
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("manage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html",
                  context={"login_form": form})
