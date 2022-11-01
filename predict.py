"""
import libraries 
"""
from flask import Flask, request, jsonify
import pickle 
import pandas as pd 

input_file = 'pred_file.bin'

with open(input_file, 'rb') as file:
    sc, model = pickle.load(file)

app = Flask("price_class")

@app.route('/', methods=["POST"])

def predict_class():
    device = request.get_json()

    df_dict = pd.DataFrame([device])

    X = sc.transform(df_dict)
    prediction = model.predict(X)[0]
    
    result = {
        'price_range': int(prediction)
    }

    return jsonify(result)

if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0', port=9696)

