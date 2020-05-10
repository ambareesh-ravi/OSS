from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_cache import Cache
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

cache = Cache()
cors = CORS(app)
bcrypt = Bcrypt()
jwt = JWTManager(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/login',methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg":"missing json"}), 400

    username = request.json.get('username',None)
    password = request.json.get('password',None)

    access_token = create_access_token(identity=username)
    return jsonify(token=access_token), 200

@app.route('/protected',methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200






if __name__=="__main__":
    app.run()