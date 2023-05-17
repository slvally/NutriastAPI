from flask import Flask, request, jsonify
from prediction import afunction

# Initialize Flask
app = Flask(__name__)

# Initialize Flask server (file prediction.py)
@app.route("/", methods=["POST"])
def new_world():
    return "Welcome to our API"

@app.route("/predict", methods=["POST"])
def hello():
    input = request.json['input']
   
    return jsonify(output = afunction(input))

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True) # run on GCP
    app.run(port=8080, debug=True) #run on local