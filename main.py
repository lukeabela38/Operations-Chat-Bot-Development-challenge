import os


def main() -> int:

    print("Hello, World")

    matches = []
    for root, dirnames, filenames in os.walk('funderpro_faqs'):
        print(root, dirnames, filenames)

    return 0

if __name__ == "__main__":
    main()