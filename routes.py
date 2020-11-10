from app import app
from db import db
from flask import redirect, render_template, request
import users, locations

@app.route("/")
def index():
    result = db.session.execute("SELECT location_name,address,postal_code,city FROM locations")
    location = result.fetchall()
    return render_template("index.html", location=location) 

@app.route("/new")
def new():
    return render_template("new.html")
    
@app.route("/send", methods=["POST"])
def send():
    locations.send()
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
            return render_template("error.html",message="Väärä tunnus tai salasana") 
            
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
            return render_template("error.html",message="Rekisteröinti ei onnistunut")            