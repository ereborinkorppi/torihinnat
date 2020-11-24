from db import db
from flask import request, session
from datetime import datetime
import users

def add():
    location_id = request.form["location"]
    product_id = request.form["product"]
    price = request.form["price"]
    price_unit = request.form["price_unit"]
    added = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    sql = "INSERT INTO price_info (location_id,product_id,price,price_unit,added) VALUES (:location_id,:product_id,:price,:price_unit,:added)"
    db.session.execute(sql, {"location_id":location_id,"product_id":product_id,"price":price,"price_unit":price_unit,"added":added})
    db.session.commit()

def get():
    result = db.session.execute("SELECT locations.location_name,locations.city,products.product_name,price_info.price,price_info.price_unit,price_info.added FROM price_info,locations,products WHERE price_info.product_id = products.id AND price_info.location_id = locations.id AND price_info.visible ORDER BY price_info.added DESC")
    price_line = result.fetchall()
    return price_line