from flask import Flask, Response
import requests
import json

app = Flask(__name__)

@app.route("/api")
def get_data():
    url = "https://api.odcloud.kr/api/15077756/v1/vaccine-stat"
    params = {
        "serviceKey": "여기에_당신의_API_KEY_입력",
        "page": 1,
        "perPage": 10
    }
    res = requests.get(url, params=params)
    return Response(
        json.dumps(res.json(), ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
