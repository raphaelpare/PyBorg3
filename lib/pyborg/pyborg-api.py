from flask import Flask
from flask_restful import Api, Resource, reqparse
import pyborg

app = Flask(__name__)
api = Api(app)
pyborg3 = pyborg.pyborg()

class Pyborg(Resource):

    def get(self, msg):
        msg = pyborg3.process_msg(self, msg, 100, 1, ('msg'), owner = 1)
        return msg, 200

    def output(self, message, args):
        return

    def post(self, msg):
        msg = pyborg3.process_msg(self, msg, 100, 1, ('msg'), owner = 1)
        return msg, 201

    def put(self, msg):
        pyborg3.save_all()
        return "Saved dictionnary", 201
      
api.add_resource(Pyborg, "/pyborg/<string:msg>")

app.run(debug=True)