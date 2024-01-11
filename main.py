# AdGuard Home - Add DDNS IP as allowed client
# Michi von Ah - January 2024
# AdGuard API Documentation (inofficial): https://fossies.org/linux/AdGuardHome/AGHTechDoc.md#list-access-settings

# Import modules
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import dns
import dns.resolver

# Load envirommental variables
load_dotenv()

# Global defintions
API_BASE_URL = os.getenv('API_BASE_URL')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

# Get the current access list of the AdGuard Home Server
def getClients(api_base_url, api_username, api_password):
    endpoint = f"{api_base_url}/control/access/list"
    response = requests.get(endpoint, auth=HTTPBasicAuth(api_username, api_password))
    result = response.json()
    return result

# Adds the ip address from a domain name to the allowed clients list of AdGuard Home
def addClient(api_base_url, api_username, api_password, domainname):
    endpoint = f"{api_base_url}/control/access/set"

    currentList = getClients(api_base_url, api_username, api_password)
    currentAllowList = currentList["allowed_clients"]
    currentDisallowList = currentList["disallowed_clients"]
    currentBlockedHosts = currentList["blocked_hosts"]

    clientId = getIPAdress(domainname)
    if not clientId in currentAllowList:
        allowedList = currentAllowList + [clientId]

        data = {
        "allowed_clients":allowedList,
        "disallowed_clients":currentDisallowList,
        "blocked_hosts":currentBlockedHosts
        }

        response = requests.post(endpoint, auth=HTTPBasicAuth(api_username, api_password), json=data)
        if response.status_code == 200:
            return f"{clientId} successfully added to the list of allowed clients."
        else:
            return f"An error occured while adding {clientId} to the list of allowed clients. Error message: {response.text}"
    else:
        return f"{clientId} already in list of allowed clients. Nothing was changed."


# Resolves the ip address of a domainname
def getIPAdress(domainname):
    lookup = dns.resolver.resolve(domainname, 'A')
    for ipval in lookup:
        ip = ipval.to_text()
    return ip

# Main programm
if __name__ == '__main__':
    print(addClient(API_BASE_URL, API_USERNAME, API_PASSWORD, DOMAIN_NAME))