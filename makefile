all: test

#Need to download stopwords corpus for nltk

test: build
	python src/main.py

build: clean
	mkdir -p output

clean:
	rm -rf input_for_mallet.mallet output/*
