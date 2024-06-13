import requests


ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 10,
}

resp = requests.post("http://localhost:9696/predict", json=ride)
print(resp.json())
