from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def home():
    req = request.args.get('fname')
    if req == None:
        req = ""
    print(req)
    return render_template("home.html", out=req)


if __name__ == "__main__":
    app.run(debug=True)
