from django.urls import path
from .views import transactions_list

urlpatterns = [
    path('', transactions_list),
]
