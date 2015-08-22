import MalletParser
import nltk
import os
import show_word_cloud

DEBUG = True

def remove_headers(lines):
    return lines[1:]


def fetch_person(line):
    return line.split(',')[0]


def fetch_text(line):
    return ",".join(line.split(',')[3:])


def fetch_title(line):
    return line.split(',')[2]


def parse_speeches(text):
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

    return parse_speeches(text)


def parse_subjects(text):
    subjects_dict = {}

    for line in text.splitlines():
        cells = line.split(",")
        subject = cells[0]
        candidate_words = cells[1:]

        if subjects_dict.has_key(subject):
            subjects_dict[subject].extend(candidate_words)

        else:
            subjects_dict[subject] = candidate_words

    return subjects_dict


def read_subjects(input_file):
    input_handle = open(input_file, "r")
    text = None

    try:
        text = input_handle.read()

    finally:
        input_handle.close()

    return parse_subjects(text)


def fetch_words(speech_text):
    words = [word.strip(",.;") for word in speech_text.split()]
    return words


def aggregate_speeches(person_speeches_dict):
    fd = nltk.FreqDist()

    for title in person_speeches_dict.keys():
        speech_text = person_speeches_dict[title]
        fd += nltk.FreqDist(fetch_words(speech_text))

    return fd


def create_person_df_dict(speeches_dict):
    person_df_dict = {}

    for person in speeches_dict.keys():
        person_df_dict[person] = aggregate_speeches(speeches_dict[person])

    return person_df_dict


def calculate_subject_score(word_frequencies):
    return float(sum(word_frequencies)) / float(len(word_frequencies))

def create_subjects_score_dict(subjects_dict, word_fd):
    subjects_score_dict = {}

    for subject, words in subjects_dict.items():
        word_frequencies = [word_fd[word] for word in words]
        subjects_score_dict[subject] = calculate_subject_score(word_frequencies)

    return subjects_score_dict


def create_person_subjects_dict(subjects_dict, person_fd_dict):
    person_subjects_dict = {}

    for person, word_fd in person_fd_dict.items():
        person_subjects_dict[person] = create_subjects_score_dict(subjects_dict, word_fd)

    return person_subjects_dict


def create_freq_output_string(subjects):
    subject_list = []

    for subject, freq in subjects.items():
        subject_list += [subject.replace(" ", "_")] * int(freq)

    return " ".join(subject_list)


def main():
    INPUT_SPEECHES_FILE = "res/speeches_text.csv"
    INPUT_SUBJECTS_FILE = "res/subjects.csv"
    OUTPUT_PERSON_DIRECTORY = "output/"

    #MalletParser.createInputForMallet()
    speeches_dict = read_speeches(INPUT_SPEECHES_FILE)
    subjects_dict = read_subjects(INPUT_SUBJECTS_FILE)

    person_fd_dict = create_person_df_dict(speeches_dict)

    person_subjects = create_person_subjects_dict(subjects_dict, person_fd_dict)

    #Write persons output files
    for person, subjects in person_subjects.items():
        output_handle = open(os.path.join(OUTPUT_PERSON_DIRECTORY, person), "w")

        try:
            subject_freq_output_string = create_freq_output_string(subjects)
            output_handle.flush()
            output_handle.write(subject_freq_output_string)

        finally:
            output_handle.close()

if __name__ == "__main__":
    main()
    show_word_cloud.main()