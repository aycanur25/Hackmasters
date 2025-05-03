from flask import Flask, request, render_template_string

app = Flask(__name__)
flag = open("flag.txt").read().strip()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin' OR '1'='1":
            return f"Giriş başarılı! Flag: {flag}"
        return "Giriş başarısız."
    return '''
        <h2>Login Paneli</h2>
        <form method="POST">
        Kullanıcı: <input name="username"><br>
        Şifre: <input name="password"><br>
        <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")
