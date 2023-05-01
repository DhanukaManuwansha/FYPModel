from flask_restful import reqparse, Resource
from Prediction import  predict


class GetBodyPart(Resource):
    @staticmethod
    def post():
        getBodyPartRequest = reqparse.RequestParser()
        getBodyPartRequest.add_argument("imageString", required=True)
        args = getBodyPartRequest.parse_args()
        bone_type_result = predict(args['imageString'])
        return bone_type_result, 200





getFractureStatusRequest = reqparse.RequestParser()
getFractureStatusRequest.add_argument("imageString", required=True)
getFractureStatusRequest.add_argument("bodyPart", required=True)

class GetFractureStatus(Resource):
    @staticmethod
    def post():
        args = getFractureStatusRequest.parse_args()
        print(args['imageString'])
        bone_type_result = predict(args['imageString'], args['bodyPart'])
        return bone_type_result, 200

