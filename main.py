import requests

# URL base de la API de Google Alerts
base_url = "https://www.google.com/alerts/api/v1/alerts/"

# Tu token de autenticación (debes configurar esto adecuadamente)
auth_token = "AIzaSyDJfkt3DX_Sy87sKICNGb8ll9b0w07C5b8"

# Realiza una solicitud GET a la API para obtener las alertas
response = requests.get(base_url, headers={"Authorization": f"Bearer {auth_token}"})

if response.status_code == 200:
    alertas = response.json()
    for alerta in alertas:
        print(alerta)
else:
    print(f"Error al obtener las alertas: {response.status_code}")
