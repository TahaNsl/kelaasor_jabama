from django.urls import path
from .views import accommodations_list

urlpatterns = [
    path('', accommodations_list),
]