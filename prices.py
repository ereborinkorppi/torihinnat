from db import db
from flask import request, session
from datetime import datetime
import users

def add():
    location_id = request.form["location"]
    product_id = request.form["product"]
    price = request.form["price"]
    price_unit = request.form["price_unit"]
    added = datetime.now()
    sql = "INSERT INTO price_info (location_id,product_id,price,price_unit,added) VALUES (:location_id,:product_id,:price,:price_unit,:added)"
    db.session.execute(sql, {"location_id":location_id,"product_id":product_id,"price":price,"price_unit":price_unit,"added":added})
    db.session.commit()