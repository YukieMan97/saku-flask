from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/socialMedia")
def socialMedia():
    return render_template("socialMedia.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/hobbs")
def hobbs():
    return render_template("hobbs.html")

if __name__ == "__main__":
    app.run(debug=True)