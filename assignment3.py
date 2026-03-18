from flask import *
import os
import pymysql

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/images"

@app.route("/api/add_products",  methods = ["POST"])
def add_product():
 if request.method =="POST":
    name = request.form["name"]
    brand = request.form["brand"]
    model = request.form["model"]
    storage = request.form["storage"]
    ram = request.form["ram"]
    battery = request.form["battery"]
    price = request.form["price"]
    stock = request.form["stock"]
    photo = request.files["photo"]
    filename = photo.filename
    photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    photo.save(photo_path)
    connection = pymysql.connect(host="localhost", user="root",  database="online")

    cursor = connection.cursor()

    sql = """INSERT INTO products
             (name, brand, model, storage, ram, battery, price, stock, photo)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    data = (name, brand, model, storage, ram, battery, price, stock, photo)
    cursor.execute(sql, data)
    connection.commit()

    return jsonify({"message": "Product added successfully"})
 

app.run(debug=True)

  