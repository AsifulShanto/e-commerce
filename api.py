from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 3003))  # Use the specified port or default to 3003

# Define the base URL for the book service
BOOK_SERVICE_URL = "http://book-service:3001"

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    response = requests.get(f"{BOOK_SERVICE_URL}/books")
    return jsonify(response.json()), response.status_code

# Endpoint to get a specific book by ID
@app.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    response = requests.get(f"{BOOK_SERVICE_URL}/books/{book_id}")
    return jsonify(response.json()), response.status_code

# Endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    response = requests.post(f"{BOOK_SERVICE_URL}/books", json=data, headers={'Content-Type': 'application/json'})
    return jsonify(response.json()), response.status_code

# Endpoint to update a book by ID
@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    response = requests.put(f"{BOOK_SERVICE_URL}/books/{book_id}", json=data, headers={'Content-Type': 'application/json'})
    return jsonify(response.json()), response.status_code

# Endpoint to delete a book by ID
@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    response = requests.delete(f"{BOOK_SERVICE_URL}/books/{book_id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
