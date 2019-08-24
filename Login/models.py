from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username

class GradeMedic(models.Model):
    client_name = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=50)
    defau = 'b'
    grade = (
        ('b', 'Regular'),
        ('g', 'Bueno'),
        ('e', 'Excelente'),
    )
    grade_doctor = models.CharField(max_length=1, choices=grade, default=defau)
    def __str__(self):
        return self.client_name