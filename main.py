import requests
from requests.auth import HTTPBasicAuth

# AdGuard Home API Informationen
API_BASE_URL = ""
API_USERNAME = ""
API_PASSWORD = ""

# IP-Adresse, die zur Whitelist hinzugefügt werden soll
IP_TO_WHITELIST = "1.2.3.4"

def add_ip_to_whitelist(api_base_url, api_username, api_password, ip_to_whitelist):
    # API-Endpunkt für die Whitelist
    api_endpoint = f"{api_base_url}/control/access/whitelist/add"

    # Daten für die POST-Anfrage
    data = {
        "ip": ip_to_whitelist,
    }

    try:
        # API-Anfrage durchführen
        response = requests.post(api_endpoint, auth=HTTPBasicAuth(api_username, api_password), json=data)

        # Überprüfen, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            print(f"Erfolgreich: {ip_to_whitelist} wurde zur Whitelist hinzugefügt.")
        else:
            print(f"Fehler: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")

# Funktion aufrufen
add_ip_to_whitelist(API_BASE_URL, API_USERNAME, API_PASSWORD, IP_TO_WHITELIST)
