import json


def load_students(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        students = json.loads(file.read())
        return students


def load_professions(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        professions = json.loads(file.read())
        return professions
