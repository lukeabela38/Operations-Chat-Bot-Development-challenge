import os
from typing import Generator, Any

def get_filepaths(root_path: str = "funderpro_faqs") -> Generator[Any, Any, Any]:
    for root, _, filenames in os.walk(root_path):
        for filename in filenames:
            yield f"{root}/{filename}"

def make_query_response_dict():
    