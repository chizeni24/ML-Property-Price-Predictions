# Property Price Prediction Model with NLP and FastAPI
This is a web application deployed in Heroku using FastAPI Framework that predicts the price of a property based on certain features of the property using machine learning. 

## Model Build Architecture
![Screenshot](https://github.com/chizeni24/ML-Property-Price-Predictions/blob/main/Deployment%20Approach.png)

## Features
The app takes in the following features of the property as input:

- Location: The location of the property
- Area: The total area of the property in square feet
- Number of bedrooms: The number of bedrooms in the property
- Number of bathrooms: The number of bathrooms in the property
- Age of property: The age of the property in years
- Type of property: The type of property (apartment, house, etc.)
- Distance to nearest public transportation: The distance to the nearest public transportation (in miles)
- Distance to nearest shopping mall: The distance to the nearest shopping mall (in miles), etc.

## Aim
The app uses a machine learning model to predict the price of the property based on the above input features. The model has been trained on a dataset of properties with known prices and features and predicts range of newly listed properties based on given features 

The model uses a combination of ensemble linear regression to make its predictions. The model has an accuracy of 85% on the test dataset.

## Deployment Architect 
![Screenshot](https://github.com/chizeni24/ML-Property-Price-Predictions/blob/main/Deployment%20Architecture.png)
## Requirements
The app requires Python 3.7 or higher and all the dependencies in the requirement.txt files.
To install the app, clone this repository and navigate to the root directory of the project. Then run the following command:

### Install all required dependencies
``` markdown
pip install -r requirements.txt
```

### Execute the code
``` markdown
python engine.py 
```
```markdown 
Enter 1 to train the model
```
### To run the web application

```markdown
Enter 2 to run the FastAPI app.py file 
```

To run the app on FastAPI deployed on my Heroku click [here](https://property-price-predicting-app.herokuapp.com/docs#/default/predict_price_predict_post)  
