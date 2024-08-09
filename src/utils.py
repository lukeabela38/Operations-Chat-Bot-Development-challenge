## MISC Functions to find, load, create various files

import os, csv, json
from typing import Generator, Any

def get_filepaths(root_path: str = "funderpro_faqs") -> Generator[Any, Any, Any]:
    for root, _, filenames in os.walk(root_path):
        for filename in filenames:
            yield f"{root}/{filename}"

def get_text_from_filepath(filepath: str) -> list[str]:
    with open(filepath) as f:
        return f.readlines()

def create_query_response_dict(l: list[str], id: int) -> dict:

    query_response_dict: dict = {}

    query_response_dict["id"] = id
    query_response_dict["query"] = l[0].strip()
    query_response_dict["response"] = l[1:]

    return query_response_dict

def dicts_to_csv(dicts: list, csv_path: str) -> None:

    keys = dicts[0].keys()

    with open(csv_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts)
        
def dicts_to_json(dicts: list, json_path: str):
    with open(json_path, "w") as out_file:
        json.dump(dicts, out_file)