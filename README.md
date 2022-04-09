# HateSpeech-portuguese
Detecção de discurso de ódio em português utilizando técnicas de aprendizado de máquina.

## Desenvolvimento:
* Foi usado Python 3.8 como linguagem base;
* Foram usado bibliotecas auxiliares para a preparação dos dados (pandas, numpy, nltk, pickle);
* Para salvar os dados foi usado uma API, desenvolvida por mim e hospedada na Heroku. Para desenvoler a API foi usado Flask;
* Para a criação do modelo de predição foi usado Sklearn. Os modelos usados foram: Logistic Regression, Multinomial Naive Bayes e Linear SVC (SVM).


## Projeto:
* Projeto de Prova de conceito para o desenvolvimento de NLP's para reconhecer textos e prever os sentimentos que eles transmitem;
* Este modelo de predição faz parte de um projeto maior chamado Remote-Analyser, o qual é um sistema desenvolvido por mim, para coleta de dados suspeitos em computadores empresarias e/ou institucionais. Servindo assim, como um monitoramento mais eficiente do patrimônio destas entidades;
* Esse modelo em Python usando diversas bibliotecas específicas para auxiliar no desenvolvimento. Os classificadores foram treinado com um dataset e exportados usando pickle. O arquivo exportado foi importado em uma API construida com Flask, esta API recebe, além dos classificadores (Logistic Regression, Multinomial Naive Bayes e Linear SVC (SVM)), um body em json pelo endpoint /predict, com uma frase para prever se é um discurso de ódio ou não;
* O body de entrada para o endpoint /predict deve ser como esse:
{
  'valor': 0,
  'frase': 'Testando API'
}
* O retorno será um json como o mostrado acima, porém o 'valor' será 0 ser não for um discurso de ódio ou 1 no caso de ser.

---
## API do spyware:
* A API:
<br>Link: https://spyware-api.herokuapp.com/
* Documentação da API:
<br>Link: https://spyware-api.herokuapp.com/swagger-ui/index.html
* Repositório no GitHub:
<br>Link: https://github.com/DarlanNoetzold/spyware-API

---
## Remote-Analyser
* Repositório no GitHub:
<br>Link: https://github.com/DarlanNoetzold/Remote-Analyser
* Heroku:
<br>Link: https://remoteanalyser.herokuapp.com/home

---
⭐️ From [DarlanNoetzold](https://github.com/DarlanNoetzold)

