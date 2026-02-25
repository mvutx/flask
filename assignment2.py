from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__) 

# Configure upload folder
app.config["UPLOAD_FOLDER"] = "static/images"

# ----------------------------
# ADD SMARTPHONE (POST)
# ----------------------------
@app.route('/api/smartphones', methods=['POST'])
def add_smartphone():
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
    photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="online"
    )

    cursor = connection.cursor()

    sql = """INSERT INTO smartphones
    (name, brand, model, storage, ram, battery, price, stock, photo)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    data = (name, brand, model, storage, ram, battery, price, stock, filename)

    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Smartphone added successfully"})

# ----------------------------
# GET ALL SMARTPHONES (GET)
# ----------------------------
@app.route("/api/smartphones", methods=["GET"])
def get_smartphones():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="online"
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM smartphones")
    smartphones = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(smartphones)

# ----------------------------
# ADD LAPTOP (POST)
# ----------------------------
@app.route("/api/laptops", methods=["POST"])
def add_laptop():
    name = request.form["name"]
    brand = request.form["brand"]
    processor = request.form["processor"]
    ram = request.form["ram"]
    storage = request.form["storage"]
    screensize = request.form["screensize"]
    price = request.form["price"]
    stock = request.form["stock"]

    photo = request.files["photo"]
    filename = photo.filename
    photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="online"
    )
    cursor = connection.cursor()
    sql = """INSERT INTO laptops
    (name, brand, processor, ram, storage, screensize, price, stock, photo)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    data = (name, brand, processor, ram, storage, screensize, price, stock, filename)

    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Laptop added successfully"})

# ----------------------------
# GET ALL LAPTOPS (GET)
# ----------------------------
@app.route("/api/laptops", methods=["GET"])
def get_laptops():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="online"
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM laptops")
    laptops = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(laptops)

# ----------------------------
# RUN APPLICATION
# ----------------------------
app.run(debug=True)