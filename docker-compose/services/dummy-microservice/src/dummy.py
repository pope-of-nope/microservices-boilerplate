from flask import Flask, jsonify, request, Response, abort
import json


app = Flask('app')
try:
    from flask_cors import CORS
    CORS(app, resources={r"*": {"origins": "*"}})
except ImportError as e:
    pass


@app.route('/')
def root():
    return jsonify({"status": "okay"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
