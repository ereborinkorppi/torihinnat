from db import db
from flask import request, session
import users

def send():
    location_name = request.form["location_name"]
    address = request.form["address"]
    postal_code = request.form["postal_code"]
    city = request.form["city"]
    sql = "INSERT INTO locations (location_name,address,postal_code,city) VALUES (:location_name,:address,:postal_code,:city)"
    db.session.execute(sql, {"location_name":location_name,"address":address,"postal_code":postal_code,"city":city})
    db.session.commit()
   
