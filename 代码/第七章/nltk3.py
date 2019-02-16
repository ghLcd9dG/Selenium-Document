import nltk
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

#报错
'''
需要什么下载什么
**********************************************************************
  Resource [93mgutenberg[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('gutenberg')
  [0m
  Searched in:
    - 'C:\\Users\\xuyichenmo/nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - 'F:\\Python\\nltk_data'
    - 'F:\\Python\\share\\nltk_data'
    - 'F:\\Python\\lib\\nltk_data'
    - 'C:\\Users\\xuyichenmo\\AppData\\Roaming\\nltk_data'
**********************************************************************



>>> from nltk.book import *

*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908



text1为NLTK数据包中的一段数据源，是一大串字符串。（原文在数据包下载目录下的gutenberg.zip中的melville-moby_dick.txt）
text1.concordance('monstrous')这句话实现的是从这一大串字符串中找寻出包含monstrous这个单词的语句
'''
print(tokens)