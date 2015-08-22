import MalletParser
import nltk


def remove_headers(lines):
    return lines[1:]


def fetch_person(line):
    return line.split(',')[0]


def fetch_text(line):
    return ",".join(line.split(',')[3:])


def fetch_title(line):
    return line.split(',')[2]


def parse_csv(text):
    lines = remove_headers(text.splitlines())
    input_data_dict = {}

    for line in lines:
        #Fetching data from line
        person = fetch_person(line)
        title = fetch_title(line)
        text = fetch_text(line)

        #Adding to input_data_dict person key if not already present
        if not input_data_dict.has_key(person):
            input_data_dict[person] = {}


        input_data_dict[person][title] = text

    return input_data_dict

def read_speeches(input_file):
    input_handle = open(input_file, "r")
    text = None

    try:
        text = input_handle.read()

    finally:
        input_handle.close()

    return parse_csv(text)


def main():
    INPUT_SPEECHES_FILE = "res/speeches_text.csv"
    #MalletParser.createInputForMallet()
    speeches_dict = read_speeches(INPUT_SPEECHES_FILE)

    

if __name__ == "__main__":
    main()