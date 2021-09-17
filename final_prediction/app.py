# flask w/ model ML
from flask import Flask, request, jsonify, render_template
import joblib
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
#EGG FRITTGÅENDE
@app.route('/ml')
def ml():
    retailer_id = 345
    product_id = 295
    regular_price = 18.06
 
    quantity = 3
    limited = 1
    hasil = model.predict([[
        retailer_id, product_id, regular_price, quantity, limited
      ]])[0]
    return str(hasil)

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        body = request.json
        # 5 vars
        retailer_id = body['retailer_id']
        product_id = body['product_id']

        regular_price = body['regular_price']
        
        quantity = body['quantity']
        limited = body['limited']
        # model prediction
        hasil = model.predict([[
        retailer_id, product_id, regular_price, quantity, limited
      ]])[0]
        return jsonify({
            'retailer_id' : body['retailer_id'],
            'product_id' : body['product_id'],
           
            'regular_price' : body['regular_price'],
          
            'quantity' : body['quantity'],
            'limited' : body['limited'],
            'PRICE_PREDICTION' : hasil,
            'status': 'sukses POST'
        })
    elif request.method == 'GET':
        return jsonify({
            'status': 'Anda nge-GET'
        })
    else:
        return jsonify({
            'status': 'Anda tidak nge-POST & nge-GET'
        })

#df1['product'] = LabelEncoder().fit_transform(df1['product'])
@app.route('/predictform', methods = ['POST', 'GET'])
def predictform():
    if request.method == 'POST':
        body = request.form
        # 8 vars
        retailer_id = body['retailer_id']
        product_id = body['product_id']

        regular_price = body['regular_price']
        
        quantity = body['quantity']
        limited = body['limited']
        # model prediction
        hasil = model.predict([[
        retailer_id, product_id, regular_price, quantity, limited
      ]])[0]
        return jsonify({
            'retailer_id' : body['retailer_id'],
            'product_id' : body['product_id'],
            
            'regular_price' : body['regular_price'],
            
            'quantity' : body['quantity'],
            'limited' : body['limited'],
            'PRICE_PREDICTION' : hasil,
            'status': 'sukses POST'
        })
        # return render_template('result.html', body=body)

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(debug = True)
