# AdGuard Home - Add DDNS IP as allowed client - Docker Container
# Michi von Ah - January 2024

FROM python:3.12

# Create directory
RUN mkdir app
WORKDIR /app/

# Copy files
COPY main.py .
COPY requirements.txt .

# Set enviromental variables
ENV API_BASE_URL "https://example.com"
ENV API_USERNAME "YOUR_USERNAME"
ENV API_PASSWORD "YOUR_PASSWORD"
ENV DOMAIN_NAME "example.com"

# Install needed packages
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pip install --no-cache-dir -r requirements.txt

# Run script
CMD ["python3","main.py"]