from flask import Flask, jsonify, request
from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'superst'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)


jwt = JWTManager(app)

user = {
    'ravi':'ravikumar123',
    'lathif':'lathiflkhan'
}

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in user:
        if user[username]==password:
            create_token = create_access_token(identity=password)
            return jsonify(access_token = create_token), 200

    return jsonify(message = 'invalid credentials')


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    username = get_jwt_identity()
    return jsonify(message = f"hello, {username}! Nice to mee you")




if __name__ =='__main__':
    app.run()
