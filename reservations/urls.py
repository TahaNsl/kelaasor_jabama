from django.urls import path
from .views import my_reservations_list

urlpatterns = [
    path('my_list/', my_reservations_list),
]