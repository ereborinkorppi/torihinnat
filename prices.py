from db import db
from flask import request, session
from datetime import datetime

def add():
    location_id = request.form["location"]
    product_id = request.form["product"]
    price = request.form["price"]
    price_unit = request.form["price_unit"]
    added = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    sql = "INSERT INTO price_info (location_id,product_id,price,price_unit,added) VALUES (:location_id,:product_id,:price,:price_unit,:added)"
    db.session.execute(sql, {"location_id":location_id,"product_id":product_id,"price":price,"price_unit":price_unit,"added":added})
    db.session.commit()
    
def delete():
    price_info_id = request.form["price_info_id"]
    try:
        sql = "UPDATE price_info SET visible = NOT visible WHERE id=(:price_info_id) AND visible = TRUE"
        db.session.execute(sql, {"price_info_id":price_info_id})
        db.session.commit()
        return True
    except:
        return False    

def get():
    result = db.session.execute("SELECT locations.location_name,locations.city,products.product_name,price_info.price,price_info.price_unit,price_info.added FROM price_info,locations,products WHERE price_info.product_id = products.id AND price_info.location_id = locations.id AND price_info.visible ORDER BY price_info.added DESC")
    price_line = result.fetchall()
    return price_line
    
def get_admin():
    result = db.session.execute("SELECT locations.location_name,locations.city,products.product_name,price_info.price,price_info.price_unit,price_info.added,price_info.id FROM price_info,locations,products WHERE price_info.product_id = products.id AND price_info.location_id = locations.id AND price_info.visible ORDER BY price_info.added DESC")
    price_line = result.fetchall()
    return price_line    