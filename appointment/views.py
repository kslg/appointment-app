from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message, send_mail
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentCreationForm
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")


def appointment_template_view(request):
    # template_name = "appointment.html"
        form = AppointmentCreationForm()
        if request.method == 'POST':
            form = AppointmentCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, f"Thanks for making an appointment, we will email you ASAP!")
                return redirect('appointment')
        return render(request, 'appointment.html', {'form': form})
        #         return redirect('appointment_add')
        # return render(request, 'create.html', {'form': form})
        # pname = request.POST.get("pname")
        # cname = request.POST.get("cname")
        # clname = request.POST.get("clname")
        # tname = request.POST.get("tname")
        # date = request.POST.get("date")
        # time = request.POST.get("time")
        # email = request.POST.get("email")
        # mobile = request.POST.get("mobile")
        # comments = request.POST.get("comments")

        # appointment = Appointment.objects.create(
        #     parent_name=pname,
        #     child_name=cname,
        #     class_name=clname,
        #     teacher=tname,
        #     date=date,
        #     time=time,
        #     email=email,
        #     phone=mobile,
        #     comments=comments,
        # )

        # appointment.save()

        # messages.add_message(request, messages.SUCCESS, f"Thanks for making an appointment, we will email you ASAP!")
        # return render(request, 'appointment.html', {'form': form})
        # return HttpResponseRedirect(request.path)



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

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context


# AJAX
def load_classes(request):
    teacher_id = request.GET.get('teacher_id')
    classes = ClassName.objects.filter(teacher_id=teacher_id)
    return render(request, 'class_dropdown_list_options.html', {'classes': classes})