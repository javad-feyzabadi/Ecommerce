from django.urls import path,include

from . import views

app_name = 'orders'


urlpatterns = [
    path('card/',views.CardView.as_view(),name='card'),

]

