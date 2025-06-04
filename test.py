import requests

response = requests.post(
    "http://localhost:7860/api/predict",
    json={"data": ["Your text here"]},
    headers={"Content-Type": "application/json"}
)
print(response.json())