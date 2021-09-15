# load ML model : pickle
# import pickle

# with open('modelPickle', 'rb') as modelku:
#     modelLoad = pickle.load(modelku)

import joblib
modelLoad = joblib.load('modelJoblib')

print(modelLoad.predict([[
    345, 295, 18.09,3.0,1]])[0])

