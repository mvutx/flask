from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "static/images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------
# ADD SMARTPHONE (POST)
# ----------------------------
@app.route('/api/smartphones', methods=['POST'])
def add_smartphone():
    try:
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

        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
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
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ----------------------------
# GET ALL SMARTPHONES (GET)
# ----------------------------
@app.route("/api/smartphones", methods=["GET"])
def get_smartphones():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM smartphones")
        smartphones = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(smartphones)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ----------------------------
# ADD LAPTOP (POST)
# ----------------------------
@app.route("/api/laptops", methods=["POST"])
def add_laptop():
    try:
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

        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
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
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ----------------------------
# GET ALL LAPTOPS (GET)
# ----------------------------
@app.route("/api/laptops", methods=["GET"])
def get_laptops():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM laptops")
        laptops = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(laptops)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ----------------------------
# RUN APPLICATION
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)