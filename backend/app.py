from flask import Flask
from queries import queries_graphql
from endpoints import endpoints_flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

#MIDDLEWARE QUE CREA EL FOLDER IMAGES SI NO EXISTE
@app.before_first_request
def create_folder():
    if os.path.exists(os.getcwd() + "/files") != True or os.path.exists(os.getcwd() + "/papelera"):
        os.makedirs(os.getcwd() + "/files")
        os.makedirs(os.getcwd() + "/papelera")


if __name__ == "__main__":
    app.register_blueprint(queries_graphql)
    app.register_blueprint(endpoints_flask)
    app.run(debug=True,port=4000, host="0.0.0.0", threaded=True)    