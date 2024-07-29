from django.urls import path
from AppRheo import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros/', views.nosotros, name="Nosotros"),
    path('servicios/', views.servicios2, name="Servicios"),
    path('contacto/', views.contacto, name="Contacto"),
    path('experiencia/', views.experiencia, name="Experiencia"),
    ]