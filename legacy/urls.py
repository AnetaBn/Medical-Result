from django.urls import path
from . import views

app_name = 'legacy'
urlpatterns = [
    path('doctors/', views.indexDoctors, name='doctors'),
    path('patients/', views.indexPatients, name='patients'),
    path('studies/', views.modalities, name='modalities'),
]