from flask import Flask

app = Flask(__name__)
class VersionUtil:
    @staticmethod
    @app.route('/lib-version', methods=['GET'])
    def get_version():
        try:
            with open("VERSION.txt", "r") as file:
                return "lib-version v" + file.read().strip()
        except FileNotFoundError:
            return "Version information not found"

if __name__ == '__main__':
    app.run(debug=False)