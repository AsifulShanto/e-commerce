from flask import Flask, request, jsonify, send_file
import requests
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 3003))  # Use the specified port or default to 3003

@app.route('/')
def index():
    return send_file('public/index.html')

@app.route('/customers')
def customers():
    return send_file('public/pages/customers/customers.html')

@app.route('/books')
def books():
    return send_file('public/pages/books/books.html')

@app.route('/lends')
def lends():
    return send_file('public/pages/lends/lends.html')

@app.route('/<service>/<endpoint>', methods=['POST'])
def forward_request(service, endpoint):
    url = f'http://{service}-service:3000/{endpoint}'
    data = request.get_json()
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'Error: {response.status_code}'}), response.status_code

if __name__ == '__main__':
    app.run(port=PORT, debug=True)

