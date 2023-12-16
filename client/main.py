import os
import requests
import threading
import time
import random


def send_request(ip, http_method, uri, http_response, log_file):
    log_text = f"{ip} {http_method} {uri} {http_response}"

    payload = {"log": log_text}
    headers = {"Content-Type": "application/json"}

    response = requests.post('http://web:8000/api/data/', json=payload,
                             headers=headers)

    print(response.status_code)

    if response.status_code == 201:
        with open(log_file, 'a') as file:
            file.write(log_text + '\n')


def random_delay(max_delay):
    return random.uniform(0, max_delay) / 1000.0


num_threads = int(os.environ.get('NUMBER_OF_REQUESTS', 5))
max_delay = int(os.environ.get('MAX_DELAY_IN_MS', 1000))
log_file_path = 'logging.txt'

while True:
    for _ in range(num_threads):
        ip_address = '192.168.1.1'
        http_method = "POST"
        uri = '/api/data'
        http_response = random.choice([201, 418])

        thread = threading.Thread(target=send_request, args=(
            ip_address, http_method, uri, http_response, log_file_path))
        thread.start()
        time.sleep(random_delay(max_delay))
