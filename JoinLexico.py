import re


def parse_and_join_data(lemma, accent, definition):
    a = open(lemma, "r", encoding="utf-8").readlines()
    b = open(accent, "r", encoding="utf-8").readlines()
    c = open(definition, "r", encoding="utf-8").readlines()

    corpus = []
    for lem, acc, dfn in zip(a, b, c):
        concatenated = f"{lem.strip()}\n\t{acc.strip()} {dfn.strip()}\n"
        corpus.append(replace_characters(concatenated))
    return corpus


def color_numbers(text):
    pattern = r"(\d{1,2})\."
    replacement = r"[b][c brown]\1.[/c][/b]"
    return re.sub(pattern, replacement, text)


def replace_characters(text_line):
    new_text = text_line.replace("[", "{")
    new_text = new_text.replace("]", "}")
    new_text = color_numbers(new_text)
    return new_text


def create_dsl(filename: str, corpus: str):
    header = '#NAME "Español-Griego"\n#INDEX_LANGUAGE "Italian"\n#CONTENTS_LANGUAGE "Greek"\n'
    complete = header + corpus
    with open(f"{filename}.dsl", "w", encoding="utf-8") as out:
        out.write(complete)


if __name__ == "__main__":
    corpus = parse_and_join_data(
        "esgr-lemma.txt", "esgr-accento.txt", "esgr-definizioni.txt"
    )
    create_dsl("Dsl-EsGr", "".join(corpus[1:]))
