import json

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json_file(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)