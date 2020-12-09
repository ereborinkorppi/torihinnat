from db import db
from flask import request, session

def add():
    location_name = request.form["location_name"]
    address = request.form["address"]
    postal_code = request.form["postal_code"]
    city = request.form["city"]
    sql = "INSERT INTO locations (location_name,address,postal_code,city) VALUES (:location_name,:address,:postal_code,:city)"
    db.session.execute(sql, {"location_name":location_name,"address":address,"postal_code":postal_code,"city":city})
    db.session.commit()

def delete():
    location_id = request.form["location_id"]
    try:
        sql = "UPDATE locations SET visible = NOT visible WHERE id=(:location_id) AND visible = TRUE"
        db.session.execute(sql, {"location_id":location_id})
        db.session.commit()
        return True
    except:
        return False

def get():
    result = db.session.execute("SELECT location_name,address,postal_code,city,id FROM locations WHERE visible")
    location = result.fetchall()
    return location
    
def get_cities():
    result = db.session.execute("SELECT DISTINCT city FROM locations WHERE visible ORDER BY city")
    cities = result.fetchall()
    return cities
