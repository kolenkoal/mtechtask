import json
import requests
import schedule
import time


def fetch_and_save_data():
    try:
        response = requests.get('http://web:8000/api/data/')

        if response.status_code == 200:
            data = response.json()
            with open('./logs.txt', 'w') as file:
                file.write(json.dumps(data, indent=2) + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")


schedule.every(1).minutes.do(fetch_and_save_data)

while True:
    schedule.run_pending()
    time.sleep(1)
