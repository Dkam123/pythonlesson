from flask import Flask, render_template

app = Flask(__name__)
app.debug = True



user = {
    "name": "Michael ",
    "lastname": "Jordan ",
    "name2": "Shaquille  ",
    "lastname2": "O'Neal  ",
    "name3": "LeBron",
    "lastname3": "James",
}

@app.route("/")
def hello():
    return render_template("player.html", user=user)


@app.route("/profile")
def profile():
    return render_template("profile.html", user=user)



app.run()