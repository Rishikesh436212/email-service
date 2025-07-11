import requests

res = requests.post(
    "http://127.0.0.1:5000/send",
    json={
        "to": "rishi@example.com",
        "subject": "Test Email",
        "body": "Hi its  mock!"
    }
)

print("STATUS:", res.status_code)
print("RESPONSE:", res.json())
