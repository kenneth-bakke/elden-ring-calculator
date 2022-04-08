import os

from flask import Flask
import requests

api_url = "https://eldenring.fanapis.com/api/"
# Example req/res
# response = requests.get(api_url)
# response.json()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Home page"


@app.route("/items/<category>", methods=["GET"])
def get_category(category):
    response = requests.get(f"{api_url}{category}")
    # response.json()
    print(response.json())
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
