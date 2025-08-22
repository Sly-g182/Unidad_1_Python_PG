from django.shortcuts import render

def inicio(request):
    return render(request, "dispositivos/inicio.html")

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "sensor temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    consumo_maximo = 100

    return render(request, "dispositivos/inicio.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })
