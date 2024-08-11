## Functions for Text Processing
import re
from sentence_transformers import SentenceTransformer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from typing import Generator, Any

class LangPreprocessor():
    def __init__(self):
        self.stransformer = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.stopwords = stopwords.words('english')
        self.porter = PorterStemmer()

        self.regex_1: str = r'[^A-Za-z ]' ## keep only alpha characters and whitespaces
        self.regex_2: str = ' +' ## remove whitespaces > 1

    ## bag of words approach, maybe we can try word embeddings
    def bag_of_words(self, s: str) -> str:

        s = s.strip() ## remove whitespaces
        s = s.lower() ## remove capitalisations
        s = re.sub(self.regex_1, '', s) ## remove non-alphanumeric characters
        s = re.sub(self.regex_2, ' ', s)

        tokens: list = s.split(" ") ## tokenize

        filtered_tokens: list = [word for word in tokens if word not in self.stopwords] ## remove stopwords/common words

        ## we could have used lemmatization, but it is more computationally complex and would involve us generating POS tags
        for i in range(len(filtered_tokens)):
            filtered_tokens[i] = self.porter.stem(filtered_tokens[i]) ## port stemming
        
        return ' '.join(filtered_tokens)

    def embeddings(self, s: str) -> list:

        s = s.strip() ## remove whitespaces
        s = s.lower() ## remove capitalisations

        # Sentences are encoded by calling model.encode()
        query_embedding = self.stransformer.encode(s, convert_to_tensor=True)

        return query_embedding

    def process_dict(self, query_response_dict: dict) -> dict:

        processed_query = self.bag_of_words(query_response_dict["query"])
        processed_response = self.bag_of_words(query_response_dict["response"])

        query_response_dict["processed_query"] = processed_query
        query_response_dict["processed_response"] = processed_response
        
        return query_response_dict