from django import forms


#Formulario de contacto para envio de e-mail

class FormularioContacto(forms.Form):
    
    asunto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mensaje'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'})
    )
    
#Formulario para contar experiencia y se guarda en base de datos

class FormularioExperiencia(forms.Form):
    nombre_experiencia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cliente'})
    )
    descripcion_experiencia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experiencia'})
    )
    
    
#Formulario para consultar servicios existentes (consulta a base de datos)

class FormularioBuscaServicio(forms.Form):
    nombre_servicio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Servicio que quiere consultar si brindamos'})
    )
    