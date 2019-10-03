from flask import Flask
from flask_restful import Api, Resource, reqparse
import linda

app = Flask(__name__)
api = Api(app)
linda.connect()
blog = linda.TupleSpace()
linda.universe._out(("MicroBlog", blog))


class Blog(Resource):
    def post(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument("topico")
        parser.add_argument("mensagem")
        args = parser.parse_args()
        blog._out((user, args["topico"], args["mensagem"]))
        return 201


api.add_resource(Blog, "/blog/<string:user>")
app.run(debug=True)
