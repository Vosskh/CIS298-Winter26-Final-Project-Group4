import json


def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions