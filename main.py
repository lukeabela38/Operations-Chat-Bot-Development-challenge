from tqdm import tqdm
from dotenv import dotenv_values

from src.elastic import ELK
from src.nlp import LangPreprocessor
from src.utils import get_filepaths, get_text_from_filepath, create_query_response_dict, dicts_to_csv, dicts_to_json

ROOT_PATH: str = "funderpro_faqs"
CSV_PATH: str = "artifacts/data.csv"
JSON_PATH: str = "artifacts/data.json"
ENV_PATH: str = ".env"

def main() -> int:

    config = dotenv_values(ENV_PATH)  

    lp = LangPreprocessor()
    elk = ELK(config=config)
    elk.establish_es_connection()

    elk.delete_index()
    elk.create_index()

    filepaths: list = list(get_filepaths(ROOT_PATH))
    dicts: list = []

    for i in tqdm(range(len(filepaths))):

        filepath = filepaths[i]
        text: str = get_text_from_filepath(filepath)
        dict = create_query_response_dict(text)
        dict = lp.process_dict(dict)

        elk.index_document(dict)

        dicts.append(dict)

    elk.refresh_index()
    
    dicts_to_csv(dicts, csv_path=CSV_PATH)
    dicts_to_json(dicts, JSON_PATH)

    responses = elk.search_index(query="Leverage?")
    for response in responses:
        print(response["_source"]["query"])
        print(response["_source"]["response"])
    

    return 0

if __name__ == "__main__":
    main()