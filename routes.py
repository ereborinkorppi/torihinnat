from app import app
from db import db
from flask import redirect, render_template, request, flash, session
import users, locations, products, prices

@app.route("/")
def index():
    return render_template("index.html", location=locations.get(), price_line=prices.get()) 
    
@app.route("/add_location", methods=["GET","POST"])
def add_location():
    if request.method == "GET":
        return render_template("new_location.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            locations.add()
            return redirect("/")
    
@app.route("/del_location", methods=["POST"])
def del_location():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    else:
        if locations.delete():
            return redirect("/admin")
        else:
            flash("Virheellinen myyntipaikan id")
            return redirect("/admin")   

@app.route("/admin")
def admin():
    return render_template("admin.html", product=products.get(), location=locations.get(), price_line=prices.get()) 

@app.route("/add_product", methods=["POST"])
def add_product():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    else:
        products.add()
        return redirect("/admin")

@app.route("/del_product", methods=["POST"])
def del_product():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    else:
        if products.delete():
            return redirect("/admin")
        else:
            flash("Virheellinen tuotteen id")
            return redirect("/admin") 

@app.route("/del_price_line", methods=["POST"])
def del_price_line():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    else:
        if prices.delete():
            return redirect("/admin")
        else:
            flash("Virheellinen hintatiedon id")
            return redirect("/admin")         

@app.route("/add_price", methods=["GET","POST"])
def add_price():
    if request.method == "GET":
        return render_template("new_price.html", location=locations.get(), product=products.get())
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            prices.add()
            return redirect("/")

@app.route("/prices", methods=["GET","POST"])
def price_info():
    if request.method == "GET":
        return render_template("prices.html", price_line=prices.get_all())
    if request.method == "POST":
        return render_template("prices.html", price_line=prices.get_all())        
    
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
    if session.get("user_id"):
        users.logout()
        return redirect("/")
    else:
        return render_template("index.html", location=locations.get(), price_line=prices.get())

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
         