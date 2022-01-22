import re
import string
import pandas as pd
import nltk
import argparse
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('wordnet')

def clean_text(text):
    text=re.sub('<.*?>', ' ', text)
    text = text.translate(str.maketrans(' ',' ',string.punctuation))
    text = re.sub('[^a-zA-Z]',' ',text)
    text = re.sub("\n"," ",text)
    text = text.lower()
    text=' '.join(text.split())
    return text


def process(path="Marketer\data\dataset\twitter_results.csv"):
    df = pd.read_csv(path)
    df.iloc[:,2] = df.iloc[:,2].apply(clean_text)

    lemmatizer = WordNetLemmatizer()
    tokenizer = RegexpTokenizer(r'\w+')
    df.iloc[:,2] = df.iloc[:,2].apply(lambda x: tokenizer.tokenize(x))

    stop_words = set(stopwords.words('english'))
    df.iloc[:,2] = df.iloc[:,2].apply(lambda x: [word if word not in stop_words else '' for word in x])

    df.iloc[:,2] = df.iloc[:,2].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

    df.iloc[:,2] = df.iloc[:,2].apply(lambda x: ' '.join([str(elem) for elem in x]))
    print(df)
    df.to_csv("Marketer/data/dataset/" + "preprocessed_twitter_data.csv",index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str,default=None, help='path to twitter data')
    args = parser.parse_args()
    process(args.path)

if __name__ == '__main__':
    main()