from flask import Flask
from flask_ngrok import run_with_ngrok
import pandas as pd

app = Flask(__name__)
run_with_ngrok(app)   # Inicia o ngrok quando o app for executado

@app.route("/index")
def read_json():
    df = pd.read_json('dados.json')
    return df.to_html()

if __name__ == '__main__':
    app.run()