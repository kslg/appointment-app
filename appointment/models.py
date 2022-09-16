from django.db import models
from django.http import request


TIME_SLOTS = (
    ('0','15:30 - 15:45'),
    ('1','15:45 - 16:00'),
    ('2','16:00 - 16:15'),
    ('3','16:15 - 16:30'),
    ('4','16:30 - 16:45'),
    ('5','16:45 - 17:00'),
)

class Teacher(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


# Create your models here.
class Appointment(models.Model):
    parent_name = models.CharField(max_length=50)
    child_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=False, null=True)
    class_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=80, choices=TIME_SLOTS, default='0')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    """Good practice to add a magic method that returns a string
       representation of an object.
    """
    def __str__(self):
            return f"Appointment for {self.child_name} in {self.class_name} with \
                {self.teacher}"
    
    class Meta:
        ordering = ["-sent_date"]