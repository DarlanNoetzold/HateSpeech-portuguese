# HateSpeech-portuguese
Detection of hate speech in Portuguese, English, and Spanish using machine learning techniques.

## Development:
* Python 3.8 was used as the base language;
* Auxiliary libraries were used for data preparation (pandas, numpy, nltk, pickle);
* An API, developed by me and hosted on Heroku, was used to save the data. Flask was used to develop the API;
* Sklearn was used for creating the prediction model. The models used were: Logistic Regression, Multinomial Naive Bayes, and Linear SVC (SVM).

## Project:
* Proof of concept project for the development of NLPs to recognize texts and predict the sentiments they convey;
* This prediction model is part of a larger project called Remote-Analyser, which is a system developed by me, for collecting suspicious data on corporate and/or institutional computers. Thus, serving as a more efficient monitoring of these entities' assets;
* This model in Python uses various specific libraries to assist in development. The classifiers were trained with a dataset and exported using pickle. The exported file was imported into an API built with Flask, this API receives, in addition to the classifiers (Logistic Regression, Multinomial Naive Bayes, and Linear SVC (SVM)), a json body through the /predict endpoint, with a phrase to predict whether it is hate speech or not;
* The input body for the /predict endpoint should be like this:
{
  'valor': 0,
  'frase': 'test API'
}
* The return will be a json like the one shown above, but the 'value' will be 0 if it is not hate speech or 1 if it is.

## How to use:
* The complete application containing all configured microservices can be obtained at [DockerHub](https://hub.docker.com/repository/docker/darlannoetzold/tcc-spyware/general).
* To run it more easily, just execute the following commands:
```
docker container run --platform=linux/amd64 -it -p 8091:8091 -p 8090:8090 -p 5000:5000 -p 9091:9090 -p 3000:3000 --name=app -d darlannoetzold/tcc-spyware:4.0

docker exec -itd app /init-spyware-api.sh
docker exec -itd app /init-remoteanalyser.sh
docker exec -itd app /init-handler-hatespeech.sh
```

---

---
## HateSpeech API:
* GitHub Repository:
<br>Link: [https://github.com/DarlanNoetzold/HateSpeech-portuguese](https://github.com/DarlanNoetzold/HateSpeech-portuguese)

---
## spyware API:
* GitHub Repository:
<br>Link: [https://github.com/DarlanNoetzold/spyware-API](https://github.com/DarlanNoetzold/spyware-API)

---
## Spyware Script:
* GitHub Repository:
<br>Link: [https://github.com/DarlanNoetzold/spyware](https://github.com/DarlanNoetzold/spyware)

---
## Remote-Analyser:
* GitHub Repository:
<br>Link: [https://github.com/DarlanNoetzold/Remote-Analyser](https://github.com/DarlanNoetzold/Remote-Analyser)

---
## Charts:
* Accuracy: ![image](https://github.com/DarlanNoetzold/HateSpeech-portuguese/assets/41628589/5de6518b-0c4a-436a-b46d-e127cfa221a9)

<br>


---
⭐️ From [DarlanNoetzold](https://github.com/DarlanNoetzold)

