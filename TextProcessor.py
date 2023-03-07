import re
import unidecode
import pandas as pd


def remove_username(frase):
    frase = re.sub(r'\@[^\s]+', ' ', frase)
    return frase

def remove_newline(frase):
    frase = frase.replace('\n', ' ')
    return frase

def only_letters(frase):
    frase = re.sub(r'[^a-záâàãéêèẽíìîĩóòõôúùũû\s]+', ' ', frase)
    return frase

def remove_link(frase):
    frase = re.sub(r'www\.?[^\s]+', ' ', frase)
    return frase

def remove_hyperlink(frase):
    frase = re.sub(r'\<.?\>', ' ', frase)
    return frase

def remove_accent(frase):
    frase = unidecode.unidecode(frase)
    return frase

def adjustment_frase(frase):
    frase = re.sub(r'\s+', ' ', frase)
    frase = frase.strip()
    return frase

def remove_spam(frase):
    frase = re.sub(r'\&amp', ' ', frase)
    frase = re.sub(r'\&lt', ' ', frase)
    frase = re.sub(r'\&gt', ' ', frase)
    frase = re.sub(r'\#follow|\#followme|\#like|\#f4f|\#photooftheday', ' ', frase)
    return frase

def remove_slangs(frase):
    frase = re.sub(r' b4 ', ' before ', frase)
    frase = re.sub(r' 2b ', ' to be ', frase)
    frase = re.sub(r' 2morrow ', ' tomorrow ', frase)
    frase = re.sub(r' rn ', ' right now ', frase)
    frase = re.sub(r' brb ', ' be right back ', frase)
    frase = re.sub(r' mb ', ' my bad ', frase)
    frase = re.sub(r' luv ', ' love ', frase)
    frase = re.sub(r' b ', ' be ', frase)
    frase = re.sub(r' r ', ' are ', frase)
    frase = re.sub(r' u ', ' you ', frase)
    frase = re.sub(r' y ', ' why ', frase)
    frase = re.sub(r' ur ', ' your ', frase)
    frase = re.sub(r' hbd ', ' happy birthday ', frase)
    frase = re.sub(r' bday ', ' birthday ', frase)
    frase = re.sub(r' bihday ', ' birthday ', frase)
    frase = re.sub(r' omg ', ' oh my god ', frase)
    frase = re.sub(r' lol ', ' laughing out loud ', frase)
    return frase

def remove_abbreviations(frase):
    frase = re.sub(r" can\'t ", " can not ", frase)
    frase = re.sub(r" i\'m ", " i am ", frase)
    frase = re.sub(r" i\'ll ", " i will ", frase)
    frase = re.sub(r" i\'d ", " i would ", frase)
    frase = re.sub(r" i\'ve ", " i have ", frase)
    frase = re.sub(r" ain\'t ", " am not ", frase)
    frase = re.sub(r" haven\'t ", " have not ", frase)
    frase = re.sub(r" hasn\'t ", " has not ", frase)
    frase = re.sub(r" can\'t ", " can not ", frase)
    frase = re.sub(r" won\'t ", " will not ", frase)
    frase = re.sub(r" you\'re ", " you are ", frase)
    frase = re.sub(r" we\'re ", " we are ", frase)
    frase = re.sub(r" they\'re ", " they are ", frase)
    frase = re.sub(r" he\'s ", " he is ", frase)
    frase = re.sub(r" she\'s ", " she is ", frase)
    frase = re.sub(r" it\'s ", " it is ", frase)
    frase = re.sub(r" don\'t ", " do not ", frase)
    frase = re.sub(r" doesn\'t ", " does not ", frase)
    frase = re.sub(r" wouldn\'t ", " would not ", frase)
    frase = re.sub(r" couldn\'t ", " could not ", frase)
    frase = re.sub(r" shouldn\'t ", " should not ", frase)
    return frase

def remove_one_len_word(frase):
    frase = re.sub(r'\b[a-z]\b', ' ', frase)
    return frase

def preprocessing(data):
    data['cleaned_tweet'] = data['frase'].apply(str)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(lambda x: x.lower())
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_newline)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_hyperlink)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_spam)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_link)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_username)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_abbreviations)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(only_letters)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_accent)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_slangs)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(remove_one_len_word)
    data['cleaned_tweet'] = data['cleaned_tweet'].apply(adjustment_frase)
    return data

def init():
    df1 = pd.read_csv("base/base_dados.csv", encoding = 'utf-8')

    df2 = pd.read_csv('base/base_dados2.csv')
    df2 = df2.drop(columns=["Sexism","Body","Racism","Ideology","Homophobia","Origin","Religion","Health","OtherLifestyle","Aborting.women","Agnostic","Argentines","Asians","Autists","Black.Women","Blond.women","Brazilians.women","Chinese","Criminals","Egyptians","Fat.people","Football.players.women","Gamers","Homeless","Homeless.women","Indigenous","Iranians","Japaneses","Jews","Jornalists","Latins","Left.wing.ideology","Men.Feminists","Mexicans","Muslims.women","Nordestines","Old.people","Polyamorous","Poor.people","Rural.people","Russians","Sertanejos","Street.artist","Ucranians","Vegetarians","White.people","Young.people","Old.women","Ugly.people","Venezuelans","Angolans","Black.people","Disabled.people","Fat.women","Feminists","Gays","Immigrants","Islamists","Lesbians","Men","Muslims","Refugees","Trans.women","Travestis","Women","Bissexuals","Transexuals","Ugly.women","Thin.women","Arabic","East.europeans","Africans","South.Americans","Brazilians","Migrants","Homossexuals","Thin.people","Ageing"])

    df2.rename(columns={'frase': 'frase'})
    df2.rename(columns={'Hate.speech': 'valor'})

    data = df1.append([df2])
    data = data.drop(columns=['text', 'Hate.speech'])


    preprocessed_data = data.copy()
    preprocessed_data = preprocessing(preprocessed_data)
    preprocessed_data = preprocessed_data.replace('None', pd.NA)
    preprocessed_data = preprocessed_data.dropna()
    preprocessed_data = preprocessed_data.drop_duplicates()
    preprocessed_data = preprocessed_data.drop(columns=['frase'])
    preprocessed_data = preprocessed_data.rename(columns={'cleaned_tweet': 'frase'})

    return preprocessed_data

def init_en():
    df1 = pd.read_csv("base_en/labeled_data.csv", encoding='utf-8')

    data = df1.drop(columns=["id","count","hate_speech","offensive_language","class"])

    valor = []
    for row in data['neither']:
        if row < 3:
            valor.append(1)
        else:
            valor.append(0)

    data['valor'] = valor
    data.rename(columns={'tweet': 'frase'})

    preprocessed_data = data.copy()
    preprocessed_data = preprocessing(preprocessed_data)
    preprocessed_data = preprocessed_data.replace('None', pd.NA)
    preprocessed_data = preprocessed_data.dropna()
    preprocessed_data = preprocessed_data.drop_duplicates()
    preprocessed_data = preprocessed_data.drop(columns=['frase'])
    preprocessed_data = preprocessed_data.rename(columns={'cleaned_tweet': 'frase'})

    return preprocessed_data


def init_sp():
    data = []
    with open(f'base_sp/data_sp.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            id_, frase, valor = line.strip().split(';||;')
            data.append({'frase': frase, 'valor': int(valor)})

    data = pd.DataFrame(data)
    preprocessed_data = data.copy()
    preprocessed_data = preprocessing(preprocessed_data)
    preprocessed_data = preprocessed_data.replace('None', pd.NA)
    preprocessed_data = preprocessed_data.dropna()
    preprocessed_data = preprocessed_data.drop_duplicates()
    preprocessed_data = preprocessed_data.drop(columns=['frase'])
    preprocessed_data = preprocessed_data.rename(columns={'cleaned_tweet': 'frase'})

    return preprocessed_data