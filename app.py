from flask import Flask, request, jsonify

app = Flask(__name__)

# Data disimpan di RAM
user_intents = {}

# Dummy intent extractor (pakai keyword sederhana)
def extract_intent(message):
    message = message.lower()
    if "pizza" in message:
        return "order_pizza"
    elif "weather" in message:
        return "check_weather"
    else:
        return "unknown"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")

    intent = extract_intent(message)

    # Tambahkan intent ke memori
    if user_id not in user_intents:
        user_intents[user_id] = {}
    user_intents[user_id][intent] = user_intents[user_id].get(intent, 0) + 1

    return jsonify({
        "status": "ok",
        "parsed_intent": intent
    })

@app.route("/top-intent/<user_id>", methods=["GET"])
def top_intent(user_id):
    if user_id not in user_intents:
        return jsonify({"error": "user not found"}), 404
    
    intents = user_intents[user_id]
    top = max(intents.items(), key=lambda x: x[1])
    return jsonify({"top_intent": top[0]})

if __name__ == "__main__":
    app.run(debug=True)
