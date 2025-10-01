from flask import Flask, render_template, request
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/2b713c62b6c8a8f953d1").json()

OWN_EMAIL = os.getenv("OWN_EMAIL")
OWN_PASSWORD = os.getenv("OWN_PASSWORD")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    body = f"Nombre: {name}\nEmail: {email}\nTeléfono: {phone}\nMensaje:\n{message}"
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "New Message"
    msg["From"] = OWN_EMAIL
    msg["To"] = OWN_EMAIL 

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, msg.as_string())

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5002)