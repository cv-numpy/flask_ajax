from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_1():
    data = request.get_json()
  
    return jsonify(result='response_from_flask!')
