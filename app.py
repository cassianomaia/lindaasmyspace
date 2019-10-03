from flask import Flask
from flask_restful import Api, Resource, reqparse
import linda

app = Flask(__name__)
api = Api(app)
linda.connect()
blog = linda.TupleSpace()
linda.universe._out(("MicroBlog", blog))


class Blog(Resource):
    def get(self, name):

        return 0

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("topico")
        parser.add_argument("mensagem")
        args = parser.parse_args()

    def delete(self, name):
        return 0


api.add_resource(Blog, "/blog/<string:user>")
app.run(debug=True)
