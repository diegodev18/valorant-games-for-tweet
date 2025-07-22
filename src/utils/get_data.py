from json import load
from os import path

def get_data(path_name: str) -> dict:
    final_path_name = f"src/data/{path_name}.json"
    if path.exists(final_path_name):
        with open(final_path_name, "r") as file:
            return load(file)
    raise FileNotFoundError(f"File not found: {final_path_name}")

if __name__ == "__main__":
    print(get_data("phrases"))
    print(get_data("at_signs"))
    print(get_data("tournaments"))
