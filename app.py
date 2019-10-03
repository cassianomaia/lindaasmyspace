from flask import Flask, json
from flask_restful import Api, Resource, reqparse
import linda

app = Flask(__name__)
api = Api(app)
linda.connect()
blog = linda.TupleSpace()
linda.universe._out(("MicroBlog", blog))


class Blog(Resource):
    def get(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument("topico")
        args = parser.parse_args()
        message = blog._rd((user,args["topico"],str))
        messages = message.splitlines()
        if len(messages) > 0:
            response = app.response_class(
                response=json.dumps(messages),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            return 404

    def post(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument("topico")
        parser.add_argument("mensagem")
        args = parser.parse_args()
        blog._out((user, args["topico"], args["mensagem"]))
        return 201

    def delete(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument("topico")
        parser.add_argument("mensagem")
        args = parser.parse_args()
        blog._in((user, args["topico"], args["mensagem"]))
        return "Mensagem deletada", 200

api.add_resource(Blog, "/blog/<string:user>")
app.run(debug=True)
