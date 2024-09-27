import re

# lemma = "es-gr-lemma.txt"
# accento = "es-gr-accento.txt"
# definizioni = "es-gr-definizioni.txt"

# lemma_list = open(lemma, "r", encoding="utf-8").readlines()
# accento_list = open(accento, "r", encoding="utf-8").readlines()
# definizioni_list = open(definizioni, "r", encoding="utf-8").readlines()


def read_files(
    lemmafile="es-gr-lemma.txt",
    accentofile="es-gr-accento.txt",
    definizionifile="es-gr-definizioni.txt",
):
    lemma_list = open(lemmafile, "r", encoding="utf-8").readlines()
    accento_list = open(accentofile, "r", encoding="utf-8").readlines()
    definizioni_list = open(definizionifile, "r", encoding="utf-8").readlines()
    return lemma_list, accento_list, definizioni_list


# Παρέμβαση Κώστας
def format_accento_list(accento_list: list):
    return [format_accento_string(accento) for accento in accento_list]


def format_accento_string(input_string):
    pattern = r"\[(.*?)\]"
    replacement = r"/[i][c maroon]\1[/c][/i]/"
    output_string = re.sub(pattern, replacement, input_string)
    return output_string


def format_definizione_list(definizioni_list: list):
    return [format_definizione_string(definizione) for definizione in definizioni_list]


def format_definizione_string(input_string):
    pattern = r"(\d{1,2})\."
    replacement = r"[b][c brown]\1.[/c][/b]"
    return re.sub(pattern, replacement, input_string)


# def format_file(text_line):
#     new_text = text_line.replace("[", "/")
#     new_text = new_text.replace("]", "/")
#     pattern = r"(\d{1,2})\."
#     replacement = r"[b][c brown]\1.[/c][/b]"
#     new_text = re.sub(pattern, replacement, new_text)
#     return new_text


# def parse_and_join_data():
#     # Παρέμβαση Κώστας
#     accento_list = format_accento_list()

#     for lem, acc, dfn in zip(lemma_list, accento_list, definizioni_list):
#         concatenated = f"{lem.strip()}\n\t{acc.strip()} {dfn.strip()}\n"
#         corpus.append(concatenated)
#         # corpus.append(format_file(concatenated))
#     return corpus


def create_file(file_name: str, corpus: str):
    FILE_HEADER = '#NAME "Español-Griego"\n#INDEX_LANGUAGE "Italian"\n#CONTENTS_LANGUAGE "Greek"\n'
    complete = FILE_HEADER + corpus
    with open(f"{file_name}.dsl", "w", encoding="utf-8") as out:
        out.write(complete)


def main():
    corpus = []
    lemma_list, accento_list, definizioni_list = read_files()
    accento_list_formatted = format_accento_list(accento_list)
    definizioni_list_formatted = format_definizione_list(definizioni_list)
    for lem, acc, dfn in zip(
        lemma_list, accento_list_formatted, definizioni_list_formatted
    ):
        concatenated = f"{lem.strip()}\n\t{acc.strip()} {dfn.strip()}\n"
        corpus.append(concatenated)
    return corpus


if __name__ == "__main__":
    corpus = main()  # parse_and_join_data()
    create_file("es-gr-dls", "".join(corpus[1:]))
