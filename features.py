import os
import numpy as np
import csv
import nltk
import re


# Tokenizers

from nltk.tokenize import word_tokenize, sent_tokenize

def get_words(data):
	return word_tokenize(data)

def get_sentences(data):
	return sent_tokenize(data)

# Direct data based features

def title_length(data):
	chars = len(data.split())
	return chars, len(data)

def article_length(data):
	return len(data)

# Word token based features

def get_tags(tokens):
	return nltk.pos_tag(tokens)

def ttr(tokens):
	types = sorted(set(tokens))
	if len(tokens) != 0:           # Sort all tokens to get number of unique words
		return len(types)/len(tokens)
	return 0

def longest_word_lengths(tokens, num=2):
	lengths = [len(token) for token in tokens]
	lengths.sort(reverse=True)
	return lengths[:num]

def zipf(tokens):
	from nltk import FreqDist            # For frequenct distribution
	p = FreqDist(tokens)                 # Finding frequency distribution of the tokens found above
	freq = list(p.values())

	freq.sort(reverse=True)              # Sort freq reverse to get ranked values

	f = np.array(freq)
	r = np.arange(1, len(f)+1)

	k = np.median(f*r)
	return k

def heap(tokens):
	unique = []

	words = []
	vocab = []

	curr_word = 0
	curr_uniq = 0

	for token in tokens:
		curr_word = curr_word + 1
		if token not in unique:
			unique.append(token)
			curr_uniq = curr_uniq + 1
	
		vocab.append(curr_uniq)
		words.append(curr_word)

	V = np.array(vocab)
	N = np.array(words)

	# Using Least Squares Method, the above line has slope and intercept as follows

	n = np.log(N)
	v = np.log(V)

	k = (((np.mean(n)*np.mean(v)) - np.mean(n*v)) / ((np.mean(n)*np.mean(n)) - np.mean(n*n)))
	    
	b = np.mean(v) - k*np.mean(n)

	return k, b



# Sentence token based features

def get_sent_lengths(sents):
	lengths = [len(sent) for sent in sents]
	lengths.sort(reverse=True)
	return lengths

def longest_sent_lengths(sents):
	lengths = get_sent_lengths(sents)
	return lengths[:2]

def avg_sent_length(sents):
	lengths = get_sent_lengths(sents)
	if len(lengths) == 0:
		return 0
	return sum(lengths)/len(lengths)





TW = "/home/manas/Semester VII/Natural Language Processing/16110031_local.csv"
LI = "/home/manas/Semester VII/Natural Language Processing/Project/Data Extraction/Links/3D Printing in Medicine.csv"
CA = "/home/manas/Semester VII/Natural Language Processing/Project/Cancer.csv"

with open(CA,"r") as f:
	# for row in f:
	# 	s = row
	# 	print(s)
	# 	print("\n")
	reader=csv.reader(f)
	for idx, row in enumerate(reader):
		# print(row[1]),
		# print(nltk.pos_tag(row[1].split(" ")))
		if idx==0:
			continue

		data = re.sub(r'[^A-Za-z0-9. ]+', ' ', row[1])
		data = " ".join(data.split())

		words = get_words(data)
		sentences = get_sentences(data)

		tags = get_tags(words)
		print(idx, data[:20]) 
		# print(tags)
		# print()

		dist={}
		possible_tags= set([tag[1] for tag in tags])
		for tag  in possible_tags:
			try:
				dist[tag] += 1
			except:
				dist[tag] = 1

		# print(dist)
		head = ["Number of Tokens","Article Length", "TTR", "longest_word_lengths", "Zipf", "heap", "longest_sent_lengths", "avg_sent_length" ]
		values = [len(words), article_length(data), ttr(words), longest_word_lengths(words), zipf(words), heap(words), longest_sent_lengths(sentences), avg_sent_length(sentences)]

		for i in range(len(head)):
			print(head[i],": ",values[i])

		print()

		