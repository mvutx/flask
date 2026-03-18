@app.route("/api/get_product/<int:id>", methods=["GET"])
def get_product(id):

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="online"
    )

    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM products WHERE id = %s"
    cursor.execute(sql, (id,))

    product = cursor.fetchone()

    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404