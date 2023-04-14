import uvicorn
from fastapi import FastAPI
from PropertyVariables import ProperyPricePred
import pandas as pd
import joblib

# 1.  Creating the App object
PropertyPricePredApp = FastAPI()

# 2.  Load the model from disk
fileName = 'property_price_prediction_voting.sav'
loaded_model = joblib.load(fileName)



# 3. Index route, opens automatically on http://127.0.0.1:8000
@PropertyPricePredApp.get('/')
def index():
    return {'message': 'Hello, World!'}

# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted price with the confidence (http://127.0.0.1:8000/predict)
@PropertyPricePredApp.post('/predict')
def predict_price(data: ProperyPricePred):
    data = data.dict()
    print(data)
    data = pd.DataFrame([data])
    print(data.head())

    prediction = loaded_model.predict(data)
    print(str(prediction))
    return str(prediction)


# # 5. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8005
if __name__ == '__main__':
    uvicorn.run("app:PropertyPricePredApp",host='127.0.0.1', debug=True,port=8005, reload=True, workers=3)
