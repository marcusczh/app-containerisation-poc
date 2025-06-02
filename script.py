import requests
import time

URL = "http://localhost:8080"
TOTAL_REQ = 100
DELAY = 0.5

for i in range(TOTAL_REQ):
    try:
        response = requests.get(URL)
        version = response.text
        print(version)
    except Exception as e:
        print("Request failed")

    time.sleep(DELAY)