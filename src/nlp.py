## Functions for Text Processing
import re, nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from typing import Generator, Any

# create an object of class WordNetLemmatizer
STOPWORDS = stopwords.words('english')
PORTER = PorterStemmer()
REGEX_1: str = r'[^A-Za-z ]' ## keep only alpha characters and whitespaces
REGEX_2: str = ' +' ## remove whitespaces > 1

def process_texts(sentences: list) -> list:

    processed_sentences = []
    for sentence in sentences:
        processed_sentences.append(process_text(sentence))

    return [item for sublist in processed_sentences for item in sublist]

def process_text(s: str) -> list:

    s = s.strip() ## remove whitespaces
    s = s.lower() ## remove capitalisations
    s = re.sub(REGEX_1, '', s) ## remove non-alphanumeric characters
    s = re.sub(REGEX_2, ' ', s)

    tokens = s.split(" ") ## tokenize

    filtered_tokens = [word for word in tokens if word not in STOPWORDS] ## remove stopwords/common words

    ## we could have used lemmatization, but it is more computationally complex and would involve us generating POS tags
    for i in range(len(filtered_tokens)):
        filtered_tokens[i] = PORTER.stem(filtered_tokens[i]) ## port stemming
    
    filtered_tokens = list(set(filtered_tokens)) ## remove repeated tokens

    return filtered_tokens


def process_dict(query_response_dict: dict) -> dict:

    query_tokens = process_text(query_response_dict["query"])
    response_tokens = process_texts(query_response_dict["response"])

    query_response_dict["query_tokens"] = query_tokens
    query_response_dict["response_tokens"] = response_tokens
    
    return query_response_dict