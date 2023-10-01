from flask import Flask, request

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
