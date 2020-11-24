from app import app
from db import db
from flask import redirect, render_template, request, flash
import users, locations, products, prices

@app.route("/")
def index():
    return render_template("index.html", location=locations.get_list(), price_line=prices.get()) 

@app.route("/new_location")
def new_location():
    return render_template("new_location.html")
    
@app.route("/add_location", methods=["POST"])
def add_location():
    locations.add()
    return redirect("/")
    
@app.route("/del_location", methods=["POST"])
def del_location():
    if locations.delete():
        return redirect("/admin")
    else:
        flash("Virheellinen myyntipaikan id")
        return redirect("/admin")   

@app.route("/admin")
def admin():
    return render_template("admin.html", product=products.get(), location=locations.get_admin()) 

@app.route("/add_product", methods=["POST"])
def add_product():
    products.add()
    return redirect("/admin")

@app.route("/del_product", methods=["POST"])
def del_product():
    if products.delete():
        return redirect("/admin")
    else:
        flash("Virheellinen tuotteen id")
        return redirect("/admin") 

@app.route("/new_price")
def new_price():
    return render_template("new_price.html", location=locations.get_price(), product=products.get())   

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
         