#!/usr/bin/env python2
import sys
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_cloud(person_file_path, person):
    global text, wordcloud
    # Read the whole text.
    text = open(person_file_path).read()
    wordcloud = WordCloud().generate(text)
    # Open a plot of the generated image.
    # take relative word frequencies into account, lower max_font_size
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.suptitle(person, fontsize=20, fontweight='bold')
    plt.show()

def main():
    for file in os.listdir("output"):
        person_file_path = os.path.join("output", file)
        generate_cloud(person_file_path, file)

if __name__ == "__main__":
    main()