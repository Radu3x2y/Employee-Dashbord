from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, DetailView
from employee.forms import EmployeeForm
from employee.models import Employee


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/update_employee.html'
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse('update-employee', kwargs={'pk': self.object.user.pk})

    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        user = get_object_or_404(User, pk=user_pk)
        employee, created = Employee.objects.get_or_create(user=user)
        return employee

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.object.user.first_name
        initial['last_name'] = self.object.user.last_name
        initial['email'] = self.object.user.email
        return initial


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employee/profile.html'
    model = Employee


