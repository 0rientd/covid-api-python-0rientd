from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
import json
import os
import sys
import main

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = b'1sad564as89123dkmk'
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/global')
@cross_origin()
def global_cases():
    main.main()
    try:
        print("Opening file from server", file=sys.stdout)
        file = open("app/data.json",)

    except:
        print("Opening file from localhost", file=sys.stdout)
        file = open("data.json")

    json_data = json.load(file)

    #return render_template('index.html', data = json_data)
    return jsonify(json_data)

if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=port)