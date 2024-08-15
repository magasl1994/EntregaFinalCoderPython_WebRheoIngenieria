from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from AppRheo.forms import FormularioContacto, FormularioExperiencia, FormularioBuscaServicio
from django.core.mail import send_mail
from django import forms
from AppRheo.models import Experiencia, servicios
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings





def inicio(request):
    return render(request, 'AppRheo/index.html')

def nosotros(request):
       
    return render(request, 'AppRheo/nosotros.html')

def comunidadrheo(request):
       
    return render(request, 'AppRheo/comunidadrheo.html')

def servicios2(request):
    if request.method=="POST":
        miFormulario=FormularioBuscaServicio(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre_servicio = informacion.get("nombre_servicio")
            servicios_encontrados = servicios.objects.filter(nombre_servicio__icontains=nombre_servicio)
            return render(request, "AppRheo/servicios.html", {"nombre_servicio": servicios_encontrados})
    else:
        miFormulario = FormularioBuscaServicio()
        
    return render(request, "AppRheo/servicios.html", {"miFormulario": miFormulario})


def contacto(request):
    if request.method=="POST":
        
        miFormulario=FormularioContacto(request.POST)
        
        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data
            
            send_mail(
                infForm['asunto'],
                infForm['mensaje'],
                infForm.get('email','magalilondero@gmail.com'),
                ['rheoingenieria@gmail.com'],
                )
            
            return render(request, 'AppRheo/index.html')
    
    else:
        
        miFormulario=FormularioContacto()
        
    return render(request, 'AppRheo/contacto.html', {"form":miFormulario})

@login_required
def experiencia(request):
    if request.method == 'POST':
        miFormulario = FormularioExperiencia(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nueva_experiencia = Experiencia(
                nombre_experiencia=informacion['nombre_experiencia'],
                descripcion_experiencia=informacion['descripcion_experiencia']
            )
            nueva_experiencia.save()
            return render(request, 'AppRheo/index.html')
    else:
        miFormulario = FormularioExperiencia()
    return render(request, 'AppRheo/experiencia.html', {'form': miFormulario})
    
@login_required
def download_pdf(request, filename):
    # Ruta completa del archivo en la carpeta media/pdfs
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', filename)
    
    # Verifica si el archivo existe en la ruta especificada
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='AppRheo/pdf')
    else:
        raise Http404("Archivo no encontrado")