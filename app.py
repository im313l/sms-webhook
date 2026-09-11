from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "SMS Webhook Server is running!"

@app.route("/webhook/sms", methods=["POST"])
def sms_webhook():
    data = request.get_json(silent=True)

    print("\n========== SMS RECEIVED ==========")
    print("JSON:", data)
    print("Form:", request.form.to_dict())
    print("Raw:", request.get_data(as_text=True))
    print("=================================\n")

    return jsonify({
        "success": True,
        "message": "SMS received"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
