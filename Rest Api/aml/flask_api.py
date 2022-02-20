from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
import keras
application = Flask(__name__)
@application.route('/aml', methods=['POST'])
#define function
def predict():
 if lr:
    try:
    	json_= request.json
    	print(json_)
    	query = pd.DataFrame(json_).reindex(columns=rnd_columns, fill_value=0)

    	predict = list(lr.predict(query))
    	return jsonify({'prediction': str(predict)})
    except:
    	return jsonify({'trace': traceback.format_exc()})
 else:
 	print ('Model not good')
 	return ('Model is not good')

if __name__ == "__main__":
 try:
 	port = int(sys.argv[1])
 except:
 	port = 12345 
lr =keras.models.load_model('anti-money-laundering.h5')
print("****") 
print(lr) 
print ('Model loaded')
rnd_columns = joblib.load('aml_columns.pkl') # Load “rnd_columns.pkl”
print ('Model columns loaded')
application.run(port=port, debug=True)


