from flask import Flask
from flask_restful import Api

from resources.routes import set_routes

app = Flask(__name__)
api = Api(app)



set_routes(api)

if __name__ == '__main__':
    app.run(debug=True)