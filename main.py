from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Jane'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((x for x in data if x['id'] == user_id), None)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    data.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run()