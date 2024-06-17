from django.urls import path
from userextend import views
from userextend.views import UserCreateView

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('overview/', views.overview, name='overview'),
    path('create_user/', UserCreateView.as_view(), name='create-user'),
]

