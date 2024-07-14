from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
from .constants import APPOINTMENT_STATUS, APPOINTMENT_TYPES
# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(max_length=20, choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default='Pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name}, patient : {self.patient.user.first_name}"
