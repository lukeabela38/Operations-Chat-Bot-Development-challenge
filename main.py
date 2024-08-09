from src.nlp import process_dict
from src.utils import get_filepaths, get_text_from_filepath, create_query_response_dict, dicts_to_csv
from tqdm import tqdm

ROOT_PATH: str = "funderpro_faqs"
CSV_PATH: str = "artifacts/data.csv"

def main() -> int:

    filepaths: list = list(get_filepaths(ROOT_PATH))
    dicts: list = []

    for filepath in tqdm(filepaths):
        text: str = get_text_from_filepath(filepath)
        dict = create_query_response_dict(text)
        dict = process_dict(dict)
        dicts.append(dict)
    
    dicts_to_csv(dicts, csv_path=CSV_PATH)

    return 0

if __name__ == "__main__":
    main()