from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "notechaapandimachine"

JOBS = [
    {   
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': '$ 80,000'
    },
    {   
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': '$ 110,000'
    },
    {   
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': '$ 100,000'
    },
    {   
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Fransisco, USA',
        'salary': '$ 120,000'
    },
    {
        'id': 5,
        'title': 'Cloud Engineer',
        'location': 'Rome, Italy',
        'salary': '$ 120,000'
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)