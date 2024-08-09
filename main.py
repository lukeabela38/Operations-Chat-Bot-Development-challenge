from src.utils import get_filepaths

ROOT_PATH: str = "funderpro_faqs"

def main() -> int:

    filepaths = list(get_filepaths(ROOT_PATH))


    return 0

if __name__ == "__main__":
    main()