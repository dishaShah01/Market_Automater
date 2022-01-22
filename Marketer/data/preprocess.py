import re
import string
import pandas as pd

def clean_text(text):
#will replace the html characters with " "
    text=re.sub('<.*?>', ' ', text)
    #To remove the punctuations
    text = text.translate(str.maketrans(' ',' ',string.punctuation))
    #will consider only alphabets and numerics
    text = re.sub('[^a-zA-Z]',' ',text)
    #will replace newline with space
    text = re.sub("\n"," ",text)
    #will convert to lower case
    text = text.lower()
    # will split and join the words
    text=' '.join(text.split())
    return text
#Running the Funtion

def main(path):
    df = pd.read_csv(path)
    df.iloc[:,2].apply(clean_text)

if __name__ == '__main__':
    pass