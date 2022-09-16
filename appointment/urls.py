from . import views
from django.urls import path
from .views import  appointment_template_view, HomeTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", views.appointment_template_view, name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'), # AJAX
]