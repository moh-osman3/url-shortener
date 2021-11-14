from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

url2short = {}
port_no = 5000
HTTPS_STRING_LITERAL="https://"
@app.route("/")

def home():
    dct = {}
    req = request.args.get('fname')
    if req == None:
        req = ""
    id_endpt = hashlib.sha256(req.encode('utf-8')).hexdigest()[:4]

    if id_endpt not in url2short:
        url2short[id_endpt] = req

    return render_template("home.html", out="localhosti:{}/{}".format(port_no, id_endpt))

@app.route("/<id>")

def red(id=None):
    if id not in url2short:
        return render_template("home.html")
    else:
        original_url = url2short[id]
        return redirect(original_url)



if __name__ == "__main__":
    app.run(debug=True)
