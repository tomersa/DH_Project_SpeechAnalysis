import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_cloud(person_file_path, person):
    global text, wordcloud
    # Read the whole text.
    person_output_file_path = u"{0}.picture.jpg".format(person_file_path)

    text = open(person_file_path).read()
    wordcloud = WordCloud().generate(text)
    # Open a plot of the generated image.
    # take relative word frequencies into account, lower max_font_size
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.suptitle(person, fontsize=20, fontweight='bold')
    # plt.show()
    plt.savefig(person_output_file_path)
    plt.close('all')

def create_world_cloud(output_person_input_for_word_cloud_directory, \
                       output_person_word_cloud, \
                       output_year_word_cloud):
    for file in os.listdir(output_person_input_for_word_cloud_directory):
        person_file_path = os.path.join(output_person_input_for_word_cloud_directory, file)
        generate_cloud(person_file_path, file)


def main(output_person_input_for_word_cloud_directory, \
         output_person_word_cloud, \
         output_year_word_cloud):

    create_world_cloud(output_person_input_for_word_cloud_directory, \
                       output_person_word_cloud, \
                       output_year_word_cloud)
