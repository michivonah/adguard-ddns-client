import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import dns
import dns.resolver

# Load envirommental variables
load_dotenv()

# AdGuard Home API Informationen
API_BASE_URL = os.getenv('API_BASE_URL')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

# IP-Adresse, die zur Whitelist hinzugefügt werden soll
IP_TO_WHITELIST = "1.2.3.4"

def add_ip_to_whitelist(api_base_url, api_username, api_password, ip_to_whitelist):
    # API-Endpunkt für die Whitelist
    api_endpoint = f"{api_base_url}/control/access/set"

    # Daten für die POST-Anfrage
    data = {
        "allowed_clients": ip_to_whitelist,
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

def getClients(api_base_url, api_username, api_password):
    endpoint = f"{api_base_url}/control/access/list"
    response = requests.get(endpoint, auth=HTTPBasicAuth(api_username, api_password))
    result = response.json()
    #return result["allowed_clients"]
    return result

def addClient(api_base_url, api_username, api_password, domainname):
    endpoint = f"{api_base_url}/control/access/set"

    currentList = getClients(api_base_url, api_username, api_password)
    currentAllowList = currentList["allowed_clients"]
    currentDisallowList = currentList["disallowed_clients"]
    currentBlockedHosts = currentList["blocked_hosts"]

    clientId = getIPAdress(domainname)
    allowedList = currentAllowList + [clientId]

    data = {
        "allowed_clients":allowedList,
        "disallowed_clients":currentDisallowList,
        "blocked_hosts":currentBlockedHosts
    }
    #return data
    response = requests.post(endpoint, auth=HTTPBasicAuth(api_username, api_password), json=data)
    return response

def getIPAdress(domainname):
    lookup = dns.resolver.resolve(domainname, 'A')
    for ipval in lookup:
        ip = ipval.to_text()
    return ip
    

# Funktion aufrufen
#add_ip_to_whitelist(API_BASE_URL, API_USERNAME, API_PASSWORD, IP_TO_WHITELIST)
#print(getClients(API_BASE_URL, API_USERNAME, API_PASSWORD))

print(addClient(API_BASE_URL, API_USERNAME, API_PASSWORD, DOMAIN_NAME))