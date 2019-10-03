from flask import Flask
from flask_restful import Api, Resource, reqparse
import linda

# Iniciando a api com Flask
app = Flask(__name__)
api = Api(app)

# Conectando com o blog para que a api faça consultas no mesmo
linda.connect()
blog = linda.TupleSpace()
linda.universe._out(("MicroBlog",blog))


class Blog(Resource):
    def get(self, name):
        return 0

    def post(self, name):
        return 0

    def delete(self, name):
        return 0


api.add_resource(Blog, "/blog/<string:user>")
app.run(debug=True)
