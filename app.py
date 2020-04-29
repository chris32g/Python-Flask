from flask import Flask, jsonify, Response
from flask import request
import json
import requests
app = Flask(__name__)


books = [
    {
        'name': 'book1',
        'price': 7.99,
        'isbn': 5468416516
    },
    {
        'name': 'book2',
        'price': 19.95,
        'isbn': 32165486
    }
]


# GET all books
@app.route('/')
def hello_world(): 
        return jsonify({'books': books})

def valid_book(book):
    if "name" in book and "price" in book and "isbn" in book:
        return True
    else:
        return False

# POST add a new book
@app.route('/books', methods = ["POST"])
def add_book():
    request_data = request.get_json()
    if (valid_book(request_data)):
        new_book = {'name': request_data['name'], 
                    'price': request_data['price'],
                    'isbn': request_data['isbn']
                    }
        books.insert(0, new_book)
        response = Response("", 201, mimetype = 'application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        return "Invalid book"


# PUT to update book by isbn        
@app.route('/books/<int:isbn>', methods = ['PUT'])
def replace_book(isbn):
    requested_book = request.get_json()
    if "name" in requested_book and "price" in requested_book:
        updated_book = {
            'name': requested_book['name'],
            'price': requested_book['price'],
            'isbn': requested_book['isbn']
        }
        i=0
        for book in books:
            if book['isbn'] == isbn:
                books[i] = updated_book
            i += 1
            response = Response("", status=204)
            return response
    else:
        response = Response("Invalid values", status=400)
        return response


# PATCH to replace a book by isbn
@app.route('/books/<int:isbn>', methods = ['PATCH'])
def patch_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if 'name' in request_data:
        updated_book['name'] = request_data['name']
    if 'price' in request_data:
        updated_book['price'] = request_data['price']
    if 'isbn' in request_data:
        updated_book['isbn'] = request_data['isbn']    
    for book in books:
        if book['isbn'] == isbn:
            book.update(updated_book)
            response = Response("", status = 204)
            response.headers['Location']= '/books/' + str(book['isbn'])
            return response


# DELETE book by isbn
@app.route('/books/<int:isbn>', methods = ['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books.pop(i)
            response = Response("", status = 204)
            return response
        i += 1
    invalid_isbn_message = {"error" : "a book with the inserted isbn was not found"}
    response = Response(json.dumps(invalid_isbn_message), status = 400, mimetype='application/json')
    return response

# GET book by isbn
@app.route('/books/<int:isbn>')
def book_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            } 
    return (jsonify(return_value))


app.run(debug=True, port=5000)
