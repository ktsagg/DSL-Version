import re


def read_files(lemmafile, accentofile, definizionifile):
    lemma_list = open(lemmafile, encoding="utf-8").readlines()
    lemma_list[0] = lemma_list[0][1:]
    accento_list = open(accentofile, encoding="utf-8").readlines()
    accento_list[0] = accento_list[0][1:]
    definizioni_list = open(definizionifile, encoding="utf-8").readlines()
    definizioni_list[0] = definizioni_list[0][1:]
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


def create_file(file_name: str, corpus: str):
    FILE_HEADER = '#NAME "Español-Griego"\n#INDEX_LANGUAGE "Italian"\n#CONTENTS_LANGUAGE "Greek"\n'
    complete = FILE_HEADER + corpus
    with open(f"{file_name}", "w", encoding="utf-8") as out:
        out.write(complete)


def main(lemmafile, accentofile, definizionifile):
    corpus = []
    lemma_list, accento_list, definizioni_list = read_files(
        lemmafile, accentofile, definizionifile
    )
    accento_list_formatted = format_accento_list(accento_list)
    definizioni_list_formatted = format_definizione_list(definizioni_list)
    for lem, acc, dfn in zip(
        lemma_list, accento_list_formatted, definizioni_list_formatted
    ):
        concatenated = f"{lem.strip()}\n\t{acc.strip()} {dfn.strip()}\n"
        corpus.append(concatenated)
    return corpus


if __name__ == "__main__":
    lemmafile = "es-gr-lemma.txt"
    accentofile = "es-gr-accento.txt"
    definizionifile = "es-gr-definizioni.txt"
    corpus = main(lemmafile, accentofile, definizionifile)
    create_file("es-gr-dsl.dsl", "".join(corpus))
