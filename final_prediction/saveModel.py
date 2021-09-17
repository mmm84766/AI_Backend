import numpy as np
import pandas as pd


# load sklearn dataset
dataset = pd.read_csv('prediction_data.csv')
#dataset.drop(['product','quantity_unit','product_id'], axis=1)



# split datasets: 90% training + 10% testing
x = dataset[['retailer_id', 'product_id','regular_price', 'quantity', 'limited']]
y = dataset['offer_price']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .02)

# linear reg model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)


# save model ML: pickle
# import pickle
# with open('modelPickle.pkl', 'wb') as modelku:
#     pickle.dump(model, modelku)

# save model : joblib
# pip install joblib
import joblib
joblib.dump(model, 'modelJoblib')


from sklearn.metrics import accuracy_score
pred_cv = model.predict(x_test)
accuracy = accuracy_score(y_test,pred_cv)
print(accuracy)
