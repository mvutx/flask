from flask import * 
app = Flask(__name__)
@app.route("/api/simple-interest", methods=["GET"])
def simple_interest():
    principal = 20000
    rate = 7
    time = 8
    interest = (principal * rate * time) / 100
    return jsonify ({"The answer is": interest})

app.run(debug=True)