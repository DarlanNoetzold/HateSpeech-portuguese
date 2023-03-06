import nltk


class TextProcessor():
<<<<<<< Updated upstream
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('rslp')
        nltk.download('punkt')
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
=======
    def __init__(self, language):
        nltk.download('stopwords')
        nltk.download('rslp')
        nltk.download('punkt')
        if language == "en":
            self.stopwords = nltk.corpus.stopwords.words('english')
        elif language == "pt":
            self.stopwords = nltk.corpus.stopwords.words('portuguese')
        elif language == "sp":
            self.stopwords = nltk.corpus.stopwords.words('spanish')
        else:
            self.stopwords = nltk.corpus.stopwords.words('english')
>>>>>>> Stashed changes
        self.stemmer = nltk.stem.RSLPStemmer()

    def vectorizeText(self, text, translater):
        vector = [0] * len(translater)
        for word in text:
            if len(word) > 0:
                source = self.stemmer.stem(word)
                if source in translater:
                    position = translater[source]
                    vector[position] += 1
        return vector

    def process(self, originalText):
        words = originalText.str.lower()
        tokenizeText = [nltk.tokenize.word_tokenize(word) for word in words]
        dict = set()

        for list in tokenizeText:
            validWords = [self.stemmer.stem(word) for word in list if word not in self.stopwords and len(word) > 2]
            dict.update(validWords)

        totalOfWords = len(dict)
        tuple = zip(dict, range(totalOfWords))
        translater = {word: index for word, index in tuple}

        return [self.vectorizeText(text, translater) for text in tokenizeText]