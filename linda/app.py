from flask import Flask
from flask_restful import Api, Resource, reqparse
import linda


class Blog(Resource):
    def get(self, name):
        return 0

    def post(self, name):
        return 0

    def delete(self, name):
        return 0


if '__name__' == '__main__':
    app = Flask(__name__)
    api = Api(app)
    linda.connect()
    blog = linda.TupleSpace()
    linda.universe._out(("MicroBlog", blog))
    api.add_resource(Blog, "/blog/<string:user>")
    app.run(debug=True)
