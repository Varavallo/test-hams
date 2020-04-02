from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

services = []

class ServiceName(Resource):

    def get(self, name):

        for x in services:
            if x['name'] == name:
                return x
        return {'name':None}, 404
    def post(self, name):

        serv = {'name': name}

        services.append(serv)

        return serv

    def delete(self, name):
        for ind,key in enumerate(services):
            if key['name'] == name:
                delete_ind = services.pop(ind)
                return{'note':'delete success'}

class AllServices(Resource):

    def get(self):
        return {'services':services}

api.add_resource(ServiceName, '/service/<string:name>')
api.add_resource(AllServices, '/services')

if __name__== '__main__':
    app.run(debug=True)
