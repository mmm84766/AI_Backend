import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import joblib


app = Flask(__name__)
api = Api(app)

model = joblib.load('modelJoblib')

class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        retailer_id = posted_data['retailer_id']
        product_id = posted_data['product_id']
        regular_price = posted_data['regular_price']
        quantity = posted_data['quantity']
        limited = posted_data['limited']

        prediction = model.predict([[retailer_id, product_id, regular_price, quantity, limited]])[0]
       

        return jsonify({
            'Prediction': prediction
        })


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)
