from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1'
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2'
    }
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    print(request.args['title'])
    print(request.args['author'])
    new_book = {
        'id': len(books) + 1,
        'title': request.args['title'],
        'author': request.args['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json.get('title', book['title'])
        book['author'] = request.json.get('author', book['author'])
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,threaded=True)
