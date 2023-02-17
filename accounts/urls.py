from django.urls import path

from . import views

app_name ='accounts'

urlpatterns = [
    path('register/',views.UserRegistrations.as_view(),name='user_register'),
]