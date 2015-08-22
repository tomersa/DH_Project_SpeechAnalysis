import os, sys

SPEECHES_PATH = 'res/barack_obama_speeches/text/'
OUTPUT_FILE = "input_for_mallet.mallet"


def fetch_subject(file):
    file = file.replace(".pdf.txt", "")
    file = file.replace(" ", "_")
    return file

def fetch_text(text):
    text = text.replace("\n", " ")
    return text

def createInputForMallet():
    output_handle = open(OUTPUT_FILE, "w")
    output_handle.flush()

    try:
        for file in os.listdir(SPEECHES_PATH):
            file_path = os.path.join(SPEECHES_PATH, file)

            file_handle = open(file_path, "r")

            try:
                subject = fetch_subject(file)
                text = fetch_text(file_handle.read())
                output_handle.write("{0} {1} {2}\n".format(subject, "X", text))

            finally:
                file_handle.close()

    finally:
        output_handle.close()

if __name__ == "__main__":
    createInputForMallet()