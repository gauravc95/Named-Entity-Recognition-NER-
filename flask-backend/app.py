from flask import Flask, render_template, request, url_for, jsonify
from flask_cors import CORS
from Controller.nerExtractorController import extract

app = Flask(__name__)
ors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/tests', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True) 
    print('data from client:', input_json['input_text'])
    entity = extract(input_json['input_text'])
    return {"extracted_entity":entity}