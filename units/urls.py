from django.urls import path
from .views import DepartmentalUnitListView

urlpatterns = [
    path('api/v1/departmental-units/', DepartmentalUnitListView.as_view(), name='departmental-unit-list'),
]