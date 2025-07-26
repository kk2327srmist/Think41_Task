from flask import Flask, request, jsonify
from database import load_data
from chatbot import handle_query

app = Flask(__name__)
products, orders, order_items, inventory = load_data()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query')
    response = handle_query(user_input, products, orders, order_items, inventory)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501)
