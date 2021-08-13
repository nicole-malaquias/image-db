from flask import Flask , jsonify
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)

@app.route('/upload')
def post_uplode():
    ...

@app.route("/files", defaults={'file': None})
@app.route("/files/<file>")
def get_files(file):
    if file :
        return jsonify(file) 
    return 'não veio nada'


