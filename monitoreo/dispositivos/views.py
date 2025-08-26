from django.shortcuts import render

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    consumo_maximo = 100

    criticos = sum(1 for d in dispositivos if d["consumo"] > consumo_maximo)

    contexto = {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo,
        "criticos": criticos,
    }
    return render(request, "dispositivos/panel.html", contexto)

