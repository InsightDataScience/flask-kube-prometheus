from flask import render_template, request, jsonify
from prometheus_client import Counter
import requests
from app import app

prom_counter = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'code'])


@app.route('/')
def index():
    label_dict = {"method": request.method,
                  "endpoint": "/",
                  "code": ""}

    prom_counter.labels(**label_dict).inc()

    return render_template('index.html')

@app.route('/get-repos', methods=["GET"])
def get_repos():
    username = request.args.get("username")

    api_url = "https://api.github.com/users/{}/repos".format(username)
    resp = requests.get(api_url)

    label_dict = {"method": "GET",
                  "endpoint": "/get-repos",
                  "code": resp.status_code}

    prom_counter.labels(**label_dict).inc()

    resp_dict = resp.json()

    repos = [x["name"] for x in resp_dict]

    return jsonify(repos=repos)

