# This HealthCheck is used by ECS to make sure the container is running

import logging

import requests

# Logging to stout
logging.basicConfig(format="{'time':'%(asctime)s', 'level': '%(levelname)s', \
                           'message': '%(message)s'}",
                    level=logging.INFO)

URL = 'http://127.0.0.1'
PORT = '8000'
TIMEOUT = 5

logging.info("Starting Health Check to %s:%s", URL, PORT)

# Health Check
response = requests.get(URL + ':' + PORT + '/health/?format=json', timeout=TIMEOUT)

if response.status_code == requests.codes.ok:
    logging.info(
        f'Health check {URL}: HTTP status code {response.status_code}')
    exit(0)
else:
    logging.error(
        f'Health check {URL}: HTTP status code {response.status_code}')
    exit(1)
