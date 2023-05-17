from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'language': 'English'
    },
    {
        'id': 2,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'language': 'English'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = [book for book in books if book['id'] == id]
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    books.append(book)
    return jsonify({'message': 'Book added successfully!'})

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    book[0]['title'] = request.json['title']
    book[0]['author'] = request.json['author']
    book[0]['language'] = request.json['language']
    return jsonify({'message': 'Book updated successfully!'})

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    book = [book for book in books if book['id'] == id]
    books.remove(book[0])
    return jsonify({'message': 'Book removed successfully!'})

if __name__ == '__main__':
    app.run(debug=True)