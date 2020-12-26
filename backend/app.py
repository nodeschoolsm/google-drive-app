from flask import Flask
from queries import queries_graphql
from endpoints import endpoints_flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



if __name__ == "__main__":
    app.register_blueprint(queries_graphql)
    app.register_blueprint(endpoints_flask)
    app.run(debug=True,port=4000, host="0.0.0.0", threaded=True)    