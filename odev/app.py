# app.py
from flask import Flask, redirect, request, jsonify, render_template, make_response
from functools import wraps
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Gerçek uygulamada güvenli bir secret key kullanın

# Örnek kullanıcı veritabanı (gerçek uygulamada bir veritabanı kullanılmalı)
users_db = {
    'admin': {
        'password': generate_password_hash('password123'),
        'name': 'Admin User'
    }
}

# Kullanıcı verileri (gerçek uygulamada bir veritabanından gelecek)
users_data = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['username'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    auth = request.form

    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify', 401)

    user = users_db.get(auth.get('username'))

    if not user:
        return make_response('Could not verify', 401)

    if check_password_hash(user['password'], auth.get('password')):
        token = jwt.encode({
            'username': auth.get('username'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])

        response = make_response(jsonify({'message': 'Login successful'}))
        response.set_cookie('token', token, httponly=True)
        return response

    return make_response('Could not verify', 401)

@app.route('/users')
@token_required
def get_users(current_user):
    return render_template('users.html', users=users_data)

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('token', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)