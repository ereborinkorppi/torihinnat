from db import db
from flask import request

def send():
    location_name = request.form["location_name"]
    sql = "INSERT INTO locations (location_name) VALUES (:location_name)"
    db.session.execute(sql, {"location_name":location_name})
    db.session.commit()
   
