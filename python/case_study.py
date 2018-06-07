from bs4 import BeautifulSoup
from urllib import request
import nltk
from nltk import word_tokenize
url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
texts = eval(soup.text)

nltk.download()
