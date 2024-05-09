from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
class VersionUtil:
    @staticmethod
    @app.route('/lib-version', methods=['GET'])
    def get_version():
        try:
            with open("VERSION.txt", "r") as file:
                return jsonify("lib-version: " + file.read().strip())
        except FileNotFoundError:
            return "Version information not found"

if __name__ == '__main__':
    app.run(debug=False)