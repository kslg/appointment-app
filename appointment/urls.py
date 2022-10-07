from . import views
from django.urls import path
from .views import appointment_template_view, HomeTemplateView,\
                    ManageAppointmentTemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", views.appointment_template_view,
         name="appointment"),
    path("manage-appointments/", login_required(
         views.ManageAppointmentTemplateView.as_view()), name="manage"),
    path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'),
    path("login/", views.login_request, name="login"),
    path('delete/<int:appointment_id>', views.delete_appointment,
         name='delete'),
]
