# import flask and its components
from flask import *
import os

# import pymysql module - helps connect python flask to mysql
import pymysql

# create flask application
app = Flask(__name__)

# configure folder where images will be stored
app.config["UPLOAD_FOLDER"] = "static/images"

# ---------------------------------------------------
# ADD SMARTPHONE
# ---------------------------------------------------
@app.route("/api/add_smartphone", methods=["POST"])
def add_smartphone():
    if request.method == "POST":

        # extract details sent from form
        name = request.form["name"]
        brand = request.form["brand"]
        model = request.form["model"]
        storage = request.form["storage"]
        ram = request.form["ram"]
        battery = request.form["battery"]
        price = request.form["price"]
        stock = request.form["stock"]

        # get photo from files
        photo = request.files["photo"]

        # get filename
        filename = photo.filename

        # create path where image will be stored
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # save photo
        photo.save(photo_path)

        # create database connection
        connection = pymysql.connect(host="localhost",user="root", password="", database="online")

        # create cursor
        cursor = connection.cursor()

        # sql query
        sql = """
        INSERT INTO smartphones
        (name, brand, model, storage, ram, battery, price, stock, photo)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # data tuple
        data = (name, brand, model, storage, ram, battery, price, stock, filename)

        # execute query
        cursor.execute(sql, data)

        # save changes
        connection.commit()

        return jsonify({"message": "Smartphone added successfully"})


# ---------------------------------------------------
# GET SMARTPHONES
# ---------------------------------------------------
@app.route("/api/get_smartphone")
def get_smartphone():
    connection = pymysql.connect(host="localhost",user="root", password="", database="online")

    # create cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # sql query
    sql = "SELECT * FROM smartphones"

    # execute query
    cursor.execute(sql)

    # fetch results
    smartphones = cursor.fetchall()

    return jsonify(smartphones)


# ---------------------------------------------------
# ADD LAPTOP
# ---------------------------------------------------
@app.route("/api/add_laptop", methods=["POST"])
def add_laptop():
    if request.method == "POST":

        # extract form details
        name = request.form["name"]
        brand = request.form["brand"]
        processor = request.form["processor"]
        ram = request.form["ram"]
        storage = request.form["storage"]
        screensize = request.form["screensize"]
        price = request.form["price"]
        stock = request.form["stock"]

        # get photo
        photo = request.files["photo"]

        # filename
        filename = photo.filename

        # create photo path
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # save image
        photo.save(photo_path)

        # connect to database
        connection = pymysql.connect(host="localhost",user="root", password="", database="online")

        # create cursor
        cursor = connection.cursor()

        # sql query
        sql = """
        INSERT INTO laptops
        (name, brand, processor, ram, storage, screensize, price, stock, photo)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # tuple data
        data = (name, brand, processor, ram, storage, screensize, price, stock, filename)

        # execute query
        cursor.execute(sql, data)

        # commit changes
        connection.commit()

        return jsonify({"message": "Laptop added successfully"})


# ---------------------------------------------------
# GET LAPTOPS
# ---------------------------------------------------
@app.route("/api/get_laptop")
def get_laptop():
    connection = pymysql.connect(host="localhost",user="root", password="", database="online")

    # create cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # sql query
    sql = "SELECT * FROM laptops"

    # execute query
    cursor.execute(sql)

    # fetch results
    laptops = cursor.fetchall()

    return jsonify(laptops)


# ---------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------
app.run(debug=True)