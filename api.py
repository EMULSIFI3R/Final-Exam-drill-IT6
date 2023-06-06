from flask import Flask, jsonify, request, Response
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET
import xml.dom.minidom

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "EMULSIFI3R1124"
app.config["MYSQL_DB"] = "mydb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    data = [{k: v.decode() if isinstance(v, bytes) else v for k, v in item.items()} for item in data]
    return data


def generate_xml_response(data_list, root_element="root"):
    root = ET.Element(root_element)
    for data in data_list:
        element = ET.SubElement(root, "venue")
        for key, value in data.items():
            sub_element = ET.SubElement(element, key)
            sub_element.text = str(value)

    xml_string = ET.tostring(root, encoding='utf-8', method='xml')
    readable_xml = xml.dom.minidom.parseString(xml_string).toprettyxml(indent="  ")

    return readable_xml


@app.route("/")
def home_page():
    return Response(
        """
    Event Planner CRUD

    ===== SELECT OPERATION =====
    [1] Add Venue
    [2] Retrieve Venue List
    [3] Update Venue
    [4] Delete Venue
    [E] Exit
    """,
        mimetype="text/plain"
    )


@app.route("/add", methods=["POST"])
def add_venue():
    format = request.args.get("format")
    if format == "xml":
        root_element = "venue"
    else:
        root_element = None

    address = request.form["address"]
    comment = request.form["comments"]
    rental_fee = request.form["rental_fee"]

    query = f"""
    INSERT INTO venue (address, comments, rental_fee)
    VALUES ('{address}', '{comment}', '{rental_fee}')
    """
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

    if format == "xml":
        return Response(generate_xml_response([{"address": address}]), mimetype="text/xml")
    else:
        return jsonify({"address": address})


@app.route("/retrieve", methods=["GET"])
def retrieve_venue():
    format = request.args.get("format")
    if format == "xml":
        root_element = "venue"
    else:
        root_element = None

    query = "SELECT * FROM venue"
    data = data_fetch(query)

    if format == "xml":
        return Response(generate_xml_response(data, root_element=root_element), mimetype="text/xml")
    else:
        return jsonify(data)
    
@app.route("/retrieve/<int:id>", methods=["GET"])
def retrieve_venue_by_id(id):
    format = request.args.get("format")
    if format == "xml":
        root_element = "venue"
    else:
        root_element = None

    query = f"SELECT * FROM venue WHERE id = {id}"
    data = data_fetch(query)

    if format == "xml":
        return Response(generate_xml_response(data, root_element=root_element), mimetype="text/xml")
    else:
        return jsonify(data)



@app.route("/update/<int:id>", methods=["PUT"])
def update_venue_by_id(id):
    format = request.args.get("format")
    if format == "xml":
        root_element = "venue"
    else:
        root_element = None

    address = request.form["address"]
    comment = request.form["comments"]
    rental_fee = request.form["rental_fee"]

    query = f"""
    UPDATE venue
    SET address = '{address}', comments = '{comment}', rental_fee = '{rental_fee}'
    WHERE id = {id}
    """
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

    if format == "xml":
        return Response(generate_xml_response([{"id": id}]), mimetype="text/xml")
    else:
        return jsonify({"id": id})



@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_venue_by_id(id):
    format = request.args.get("format")
    if format == "xml":
        root_element = "venue"
    else:
        root_element = None

    query = f"SELECT * FROM venue WHERE id = {id}"
    data = data_fetch(query)

    if not data:
        return Response("Venue not found", status=404)

    query = f"DELETE FROM venue WHERE id = {id}"
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

    if format == "xml":
        return Response(generate_xml_response([{"id": id}]), mimetype="text/xml")
    else:
        return jsonify({"id": id})



if __name__ == "__main__":
    app.run(debug=True)
