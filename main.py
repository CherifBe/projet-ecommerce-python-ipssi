from flask import Flask, render_template
#from flask_cors import CORS
from infra.db import get_session

app = Flask(__name__)
#cors = CORS(app)

@app.route("/auth")
def hello_world():
    return render_template('homepage.html.j2')

