from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm
from django.core.mail import send_mail


def enviar_correo(nombre, email):
    mensaje = f"Hola, tu mascota {nombre} ha sido registrada exitosamente."
    send_mail(
        'Registro de Mascota',
        mensaje,
        'tu_email@example.com',  
        [email],                
    )


def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'app/listar_mascotas.html', {'mascotas': mascotas})


def buscar_mascotas(request):
    query = request.GET.get('q')
    mascotas = Mascota.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'app/buscar_mascotas.html', {'mascotas': mascotas, 'query': query})


def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save()
            enviar_correo(mascota.nombre, mascota.dueño_email)
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'app/agregar_mascota.html', {'form': form})
