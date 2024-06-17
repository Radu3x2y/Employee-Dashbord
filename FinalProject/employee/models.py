from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('MKT', 'Marketing'),
        ('FIN', 'Finance'),
        ('OPS', 'Operations'),
        ('IM', 'Infrastructure Management'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    position = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
