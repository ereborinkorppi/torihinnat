from db import db
from flask import request, session

def add():
    product_name = request.form["product_name"]
    sql = "INSERT INTO products (product_name) VALUES (:product_name)"
    db.session.execute(sql, {"product_name":product_name})
    db.session.commit()

def delete():
    product_id = request.form["product_id"]
    try:
        sql = "UPDATE products SET visible = NOT visible WHERE id=(:product_id) AND visible = TRUE"
        db.session.execute(sql, {"product_id":product_id})
        db.session.commit()
        return True
    except:
        return False

def get():
    result = db.session.execute("SELECT product_name,id FROM products WHERE visible")
    product = result.fetchall()
    return product

   
