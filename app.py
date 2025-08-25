from flask import Flask,jsonify

app = Flask(__name__)



@app.route("/")
def say():
    return jsonify("hello deployment done")

@app.route("/api/<value>")
def holo(value):
    return jsonify(f"hello {value}")
    




app.run(host="0.0.0.0",port=5000)