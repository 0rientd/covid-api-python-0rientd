from flask import Flask, render_template
import json
import os
from .main import main

app = Flask(__name__)
app.secret_key = b'1sad564as89123dkmk'
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    main()
    file = open("app/data.json",)
    json_data = json.load(file)
    return render_template('index.html', data = json_data)

if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=port)