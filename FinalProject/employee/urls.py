from django.urls import path
from employee import views

urlpatterns = [
    path('update_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update-employee'),
    path('profile/<int:pk>/', views.EmployeeDetailView.as_view(), name='profile'),
]