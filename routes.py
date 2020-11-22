from app import app
from db import db
from flask import redirect, render_template, request, flash
import users, locations, products, prices

@app.route("/")
def index():
    result = db.session.execute("SELECT location_name,address,postal_code,city FROM locations WHERE visible")
    location = result.fetchall()
    result2 = db.session.execute("SELECT locations.location_name,locations.city,products.product_name,price_info.price,price_info.price_unit,price_info.added FROM price_info,locations,products WHERE price_info.product_id = products.id AND price_info.location_id = locations.id AND price_info.visible ORDER BY price_info.added DESC")
    price_line = result2.fetchall()
    return render_template("index.html", location=location, price_line=price_line) 

@app.route("/new_location")
def new_location():
    return render_template("new_location.html")
    
@app.route("/add_location", methods=["POST"])
def add_location():
    locations.add()
    return redirect("/")

@app.route("/delete_location")
def delete_location():
    result = db.session.execute("SELECT location_name,address,postal_code,city,id FROM locations WHERE visible")
    location = result.fetchall()
    return render_template("delete_location.html", location=location) 
    
@app.route("/del_location", methods=["POST"])
def del_location():
    if locations.delete():
        return redirect("/")
    else:
        flash("Virheellinen myyntipaikan id")
        return redirect("/delete_location")   

@app.route("/products")
def manage_products():
    result = db.session.execute("SELECT product_name,id FROM products WHERE visible")
    product = result.fetchall()
    return render_template("products.html", product=product) 

@app.route("/add_product", methods=["POST"])
def add_product():
    products.add()
    return redirect("/products")

@app.route("/del_product", methods=["POST"])
def del_product():
    if products.delete():
        return redirect("/products")
    else:
        flash("Virheellinen tuotteen id")
        return redirect("/products") 

@app.route("/new_price")
def new_price():
    result = db.session.execute("SELECT location_name,id FROM locations WHERE visible")
    location = result.fetchall()
    result2 = db.session.execute("SELECT product_name,id FROM products WHERE visible")
    product = result2.fetchall()
    return render_template("new_price.html", location=location, product=product)   

@app.route("/add_price", methods=["POST"])
def add_price():
    prices.add()
    return redirect("/")
    
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            flash("Väärä tunnus tai salasana")
            return render_template("login.html") 
            
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            flash("Rekisteröinti ei onnistunut")
            return render_template("register.html")    
         