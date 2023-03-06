import os
from flask import Flask, request
import pandas as pd
import pickle
import TextTokenizer as prtxt
import numpy as np
from langdetect import detect

model_pt = pickle.load(open("model/model_hate_pt.pkl", 'rb'))
model_en = pickle.load(open("model/model_hate_en.pkl", 'rb'))
model_sp = pickle.load(open("model/model_hate_sp.pkl", 'rb'))

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):
            df_raw = pd.DataFrame(test_json, index=[0])
        else:
            df_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

    application_data = df_raw

    application_text = application_data['frase']
    lang = detect(application_text)
    proc = prtxt.TextProcessor(lang)

    vectorization_text_application = proc.process(application_text)

    for i in range(2714 - len(vectorization_text_application[0])):
        vectorization_text_application[0].append('0')

    XAPP = np.array(vectorization_text_application)
    results = []
    if lang == 'pt':
        for i in range(len(model_pt)):
            results.append(model_pt[i].predict(XAPP))
    elif lang == 'en':
        for i in range(len(model_en)):
            results.append(model_en[i].predict(XAPP))
    elif lang == 'sp':
        for i in range(len(model_sp)):
            results.append(model_sp[i].predict(XAPP))
    else:
        for i in range(len(model_en)):
            results.append(model_en[i].predict(XAPP))


    df_raw['valor'] = 1
    for i in range(len(results)):
        if results[i] == 'yes':
            df_raw['valor'] = 1

    return df_raw.to_json(orient='records')


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
