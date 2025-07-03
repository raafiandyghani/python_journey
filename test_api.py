import requests

# --- Kirim pesan pertama ---
res = requests.post("http://127.0.0.1:5000/chat", json={
    "user_id": "u1",
    "message": "I want pizza"
})
print("POST /chat:", res.json())

# --- Kirim beberapa pesan ---
requests.post("http://127.0.0.1:5000/chat", json={"user_id": "u1", "message": "weather is nice"})
requests.post("http://127.0.0.1:5000/chat", json={"user_id": "u1", "message": "check weather"})
requests.post("http://127.0.0.1:5000/chat", json={"user_id": "u1", "message": "order pizza again"})

# --- Cek top intent ---
res = requests.get("http://127.0.0.1:5000/top-intent/u1")
print("GET /top-intent/u1:", res.json())
