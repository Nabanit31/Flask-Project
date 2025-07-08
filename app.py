from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def student_profile():
    return render_template(
        "profile.html",
        name = "Amit",
        age = 25,
        city = "Lajpat Nagar",
        is_topper = True,
        subjects = ["Math", "Science", "History"],
    )