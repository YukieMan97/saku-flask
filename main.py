from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

if __name__ == "__main__":
    app.run(debug=True)