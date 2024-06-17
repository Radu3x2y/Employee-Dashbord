import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from employee.models import Employee
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            rand_num = random.randint(100000, 999999)
            new_user.username = new_user.first_name[0].lower() + new_user.last_name.lower() + '_' + str(rand_num)
            new_user.save()
            employee, created = Employee.objects.get_or_create(user=new_user)

            if not created:
                employee.first_name = new_user.first_name
                employee.last_name = new_user.last_name
                employee.email = new_user.email
                employee.save()

            new_user_pk = new_user.pk
            self.success_url = reverse_lazy('update-employee', kwargs={'pk': new_user_pk})
            return super(UserCreateView, self).form_valid(form)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('overview')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def overview(request):
    user = request.user
    try:
        employee = Employee.objects.get(user=user)
        context = {'employee': employee}
    except Employee.DoesNotExist:
        context = {'error_message': 'You are not registered as an employee.'}
    return render(request, 'employee/overview.html', context)
