# Prompt: Read a json file and return it as a dictionary or list or throw an error if the read fails.

import json

def readJSON(filename: str) -> dict or list:
    with open(filename) as j:
        return(json.load(j))


if __name__ == "__main__":
    contents = readJSON("test_files/test.json")
    print(contents.get("Ford"))