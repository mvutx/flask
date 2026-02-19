# importing flask 
from flask import *

# create a web server based application
app = Flask(__name__)

#Below we create the home route
#Routing -> is maping / connecting different resources to different functions .We do this by the help of a decoorator 
@app.route("/api/home")
def home():
     return  jsonify({"message" : "Home Route accessed"})


#below is the products route
@app.route("/api/products")
def products():
     return jsonify({"message" : "Welcome to products route"})


#below is a route for addition
@app.route("/api/calc", methods=["POST"])
def calculator():
     if request.method == "POST":
          number1 = request.form["number1"]
          number2 = request.form["number2"]
          sum = int(number1) + int(number2)

          return jsonify({"the answer is ": sum})






#below will run the application
app.run(debug=True)
