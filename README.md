# AdGuard Home Whitelist DDNS Client
A script for adding a dynamic ip address as an allowed client to AdGuard Home. Useful if you host AdGuard Home on a VPS and your router doesn't supports DNS over HTTPS (DoH) or DNS over TLS (DoT).

GitHub: https://github.com/michivonah/adguard-ddns-client

You can run this python script manually or via the docker container. I recommend using the docker container. But you also can run the python script manually when you need it.

Use as docker container on your server:
1. Install docker on your system

    ```apt-get install docker.io docker-compose -y```
2. Open your cronjob

    ```crontab -e```

3. Add the following line to the cronjob of your server and change the enviromental variables for your needs

    ```0 * * * * docker run -d --rm --env API_BASE_URL="https://example.com" --env API_USERNAME=YOUR_USER --env API_PASSWORD=YOUR_PASSWORD --env DOMAIN_NAME=YOUR_DDNS_DOMAIN ghcr.io/michivonah/adguard-ddns-client:main```

    Replace `0 * * * *` to run the job more often than once a hour.
    Use `0/30 * * * *` to run the job every 30 mins or `5 * * * *` to run the job every 5 minutes. Customize it to your needs.

4. Finished. Now the cronjobs runs as defined and adds the clients ip address if it is missing to AdGuard Home's Client whitelist.

## Enviormental variables
These environment variables are supported

| Variable | Description | Example |
| --- | --- | --- |
| API_BASE_URL | The url of your AdGuard Home Server | ``https://example.com`` |
| API_USERNAME | The username of your AdGuard Home Administrator Account | ``admin`` |
| API_PASSWORD | The password of your AdGuard Home Administrator Account | ``admin123`` (use a secure password) |
| DOMAIN_NAME | Your DDNS Domain name with the ip address you want to whitelist | ``ddns.example.com`` |

> Required enviromental variables: API_BASE_URL, API_USERNAME, API_PASSWORD, DOMAIN_NAME

