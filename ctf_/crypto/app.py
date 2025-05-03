from flask import Flask, request
import base64

app = Flask(__name__)
flag = open("flag.txt").read().strip()

@app.route("/")
def home():
    return '''
    <h3>Şifreli mesaj:</h3>
    <code>{}</code><br><br>
    Cevabı buraya yaz: 
    <form method="POST" action="/check">
    <input name="flag" type="text">
    <input type="submit">
    </form>
    '''.format(base64.b64encode(flag.encode()).decode())

@app.route("/check", methods=["POST"])
def check():
    answer = request.form.get("flag")
    if answer == flag:
        return "Doğru! 🎉"
    return "Yanlış ❌"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
