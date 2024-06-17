from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee


@receiver(post_save, sender=User)
def create_or_update_employee(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Employee.objects.create(user=instance)
    elif not created and instance.is_superuser:
        try:
            instance.employee.save()
        except Employee.DoesNotExist:
            Employee.objects.create(user=instance)