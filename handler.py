import os
from flask import Flask, request
import pandas as pd
import pickle
import TextTokenizer as prtxt
import numpy as np


model = pickle.load(open("model/model_hate.pkl", 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):
            df_raw = pd.DataFrame(test_json, index=[0])
        else:
            df_raw = pd.DataFrame(test_json, columns=test_json[0].keys())


    proc = prtxt.TextProcessor()

    aplicationData = df_raw

    aplicationText = aplicationData['frase']
    vectorizationTextApplication = proc.process(aplicationText)

    for i in range(2714 - len(vectorizationTextApplication[0])):
        vectorizationTextApplication[0].append('0')

    XAPP = np.array(vectorizationTextApplication)
    results = []
    for i in range(len(model)):
        results.append(model[i].predict(XAPP))

    df_raw['valor'] = 0
    for i in range(len(results)):
        if results[i] == 'yes':
            df_raw['valor'] = 1

    return df_raw.to_json(orient='records')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)