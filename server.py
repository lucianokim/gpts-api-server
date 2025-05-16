
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api")
def call_api():
    url = "https://api.odcloud.kr/api/15077756/v1/vaccine-stat"
    params = {
        "serviceKey": "여기에_당신의_API_KEY_입력",
        "page": 1,
        "perPage": 10
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
