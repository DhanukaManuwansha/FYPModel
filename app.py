
from flask import Flask
from flask_restful import Api


from Prediction import Prediction
from Service import GetBodyPart, GetFractureStatus, SaveImage

# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

app = Flask("ModelAPI")
api = Api(app)





api.add_resource(GetBodyPart, "/Model/GetBodyPart")
api.add_resource(GetFractureStatus, "/Model/GetFractureStatus")
api.add_resource(SaveImage, "/Model/SaveImage")
if __name__ == '__main__':
    app.run()
