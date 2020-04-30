from flask import Flask, jsonify,request, Response
from bookmodel import *
from settings import *
import json
import requests
from json import JSONEncoder


# GET all books
@app.route('/')
def get_books():
    return jsonify({'books': Book.list_all_books()})

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
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
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
        Book.replace_book(isbn , requested_book['name'], requested_book['price'])
        response = Response("", status=204)
        return response
    else:
        response = Response("Invalid values", status=400)
        return response


# PATCH to replace a book by isbn
@app.route('/books/<int:isbn>', methods = ['PATCH'])
def patch_book(isbn):
    request_data = request.get_json()
    if 'name' in request_data:
        Book.update_book_name(isbn , request_data['name'])
        response = Response("", status = 204)
        response.headers['Location']= '/books/' + str(isbn)
        return response
    if 'price' in request_data:
        Book.update_book_price(isbn , request_data['price'])   
        response = Response("", status = 204)
        response.headers['Location']= '/books/' + str(isbn)
        return response


# DELETE book by isbn
@app.route('/books/<int:isbn>', methods = ['DELETE'])
def delete_book(isbn):
    if(Book.delete(isbn)):
        return Response("", status=204)
    else:
        invalid_isbn_message = {"error" : "a book with the inserted isbn was not found"}
        response = Response(json.dumps(invalid_isbn_message), status = 400, mimetype='application/json')
    return response

# GET book by isbn
@app.route('/books/<int:isbn>')
def book_isbn(isbn):
    return_value = Book.get_book(isbn)
    return (jsonify(return_value))


app.run(debug=True, port=5000)
