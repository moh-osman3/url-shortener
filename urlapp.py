from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

url2short = {}
@app.route("/")

def home():
    dct = {}
    req = request.args.get('fname')
    if req == None:
        req = ""
    id_endpt = hashlib.sha256(req.encode('utf-8')).hexdigest()[:4]

    print(id_endpt)
    if id_endpt not in url2short:
        url2short[id_endpt] = req

    return render_template("home.html", out="localhost/{}".format(id_endpt))



if __name__ == "__main__":
    app.run(debug=True)
