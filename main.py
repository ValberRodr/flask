from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_whatsapp_message():
    # Get the message from Twilio
    message = request.json["message"]

    # Respond to the message
    response = jsonify({
        "body": "Hello, world!"
    })

    return response, 200

if __name__ == "__main__":
    app.run(debug=True)
