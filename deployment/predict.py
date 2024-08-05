import joblib
import pandas as pd
import os
import sys
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler

model=joblib.load("xgboost.joblib")

def prepare_features(data):
    processed_feature = pd.DataFrame(data, index=[0])
    return processed_feature

def predict(data):
    processed_data = prepare_features(data)
    processed_data=processed_data.values[[0]]
    scaler =  StandardScaler()
    xscale=scaler.fit_transform(processed_data)
    preds = model.predict(xscale)  

    return preds[0]

app = Flask('credit-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    test = request.get_json()

    features = prepare_features(test)
    print(features.values[0])

    pred = predict(features)
    print(pred)

    if pred==1:
        score = 'GOOD CREDIT RISK'
    else:
        score = "BAD CREDIT RISK"
    
    print(score)

    result = {
        'result': score
        
    }

    return jsonify(result)
    # return test


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)