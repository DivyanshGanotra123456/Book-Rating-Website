import numpy as np
import math
import re
import string
import urllib.request
#url=input('Enter the URL to summarize')
def getdata(link):
    source=urllib.request.urlopen(link).read()
    from bs4 import BeautifulSoup
    import requests
    soup=BeautifulSoup(source,'lxml')
    # print(soup)
    print('process 1/4 completed....')
    import nltk
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    from nltk.tokenize import sent_tokenize
    from sklearn.feature_extraction.text import TfidfVectorizer
    from nltk.corpus import stopwords
    text=" "
    for paragraph in soup.find_all('p'):
        text+=paragraph.text
        #print(text)
        print('process 2/4 completed....')
    texts=text
    #nltk.download('punkt')
    sentences=sent_tokenize(texts)
    total_documents=len(sentences)

    #print(sentences)
    print('process 3/4 completed....')
    #create frequency matrix of words in each sentences
    #nltk.download('stopwords')
    def create_frequency_matrix(sentences):
        frequency_matrix={}
        for text in sentences:
            text = re.sub(r'\d+', '', text)
            stopWords=set(stopwords.words("english"))
            ps=PorterStemmer()
            for sent in sentences:
                freq_table={}
                words=word_tokenize(sent)
                for word in words:
                    word=word.lower()
                    word=ps.stem(word)
                    if word in stopWords:
                        continue
                    if word in freq_table:
                        freq_table[word]+=1
                    else:
                        freq_table[word]=1
                frequency_matrix[sent[:15]]=freq_table 
        return frequency_matrix
    #create tf-matrix
    def create_tf_matrix(frequency_matrix):
        tf_matrix={}
        for sent,f_table in frequency_matrix.items():
            tf_table={}
            count_word_in_sentences=len(f_table)
            for word,count in f_table.items():
                tf_table[word]=count/count_word_in_sentences
            tf_matrix[sent]=tf_table

        return tf_matrix
    #How many sentenes contain a word
    def create_documents_per_words(frequency_matrix):
        word_per_doc_table={}
        for sent,f_table in frequency_matrix.items():
            for word,count in f_table.items():
                if word in word_per_doc_table:
                    word_per_doc_table[word]+=1
                else:
                    word_per_doc_table[word]=1
        return word_per_doc_table
    #calculate idf and generate matrix
    def create_idf_matrix(frequency_matrix,word_per_doc_table,total_documents):
        idf_matrix={}
        for sent,f_table in frequency_matrix.items():
            idf_table={}
            for word in f_table.keys():
                idf_table[word]=math.log10(total_documents/float(word_per_doc_table[word]))
            idf_matrix[sent]=idf_table

        return idf_matrix
    #generate tf-idf matrix
    def create_tf_idf_matrix(tf_matrix,idf_matrix):
        tf_idf_matrix={}
        for (sent1,f_table1),(sent2,f_table2) in zip(tf_matrix.items(),idf_matrix.items()):
            tf_idf_table={}
            for (word1,value1),(word2,value2) in zip(f_table1.items(),f_table2.items()):
                tf_idf_table[word1]=float(value1*value2)
            tf_idf_matrix[sent1]=tf_idf_table
        return tf_idf_matrix
    # sentence scoring
    def sentence_scoring(tf_idf_matrix):
        sentence_scoring_matrix={}
        for sent,f_table in tf_idf_matrix.items():
            total_score_per_sentence=0
            count_words_in_doc=len(f_table)
            for word,score in f_table.items():
                total_score_per_sentence+=score

            sentence_scoring_matrix[sent]=total_score_per_sentence/count_words_in_doc

        return sentence_scoring_matrix
    #find the average
    def average_value(sentence_scoring_matrix):
        sumvalues=0
        for entry in sentence_scoring_matrix:
            sumvalues+=sentence_scoring_matrix[entry]

        average=sumvalues/len(sentence_scoring_matrix)

        return average
    #generate summary
    def generate_summary(sentences,sentencevalue,average):
        sentence_count=0
        summary=''
        for sentence in sentences:
            if(sentence[:15] in sentencevalue and sentencevalue[sentence[:15]]>=average):
                summary+=" "+sentence
                sentence_count+=1
        return summary

    sentences=sent_tokenize(texts)
    total_documents=len(sentences)
    #print(sentences)
    freq_matrix=create_frequency_matrix(sentences)
    #print(freq_matrix)
    tf_matrix=create_tf_matrix(freq_matrix)
    #print(tf_matrix)
    count_doc_per_words=create_documents_per_words(freq_matrix)
    #print(count_doc_per_words)
    idf_matrix=create_idf_matrix(freq_matrix,count_doc_per_words,total_documents)
    #print(idf_matrix)
    tf_idf_matrix=create_tf_idf_matrix(tf_matrix,idf_matrix)
    #print(tf_idf_matrix)
    sentence_scores=sentence_scoring(tf_idf_matrix)
    #print(sentence_scores)
    average = average_value(sentence_scores)
    #print(threshold)
    summary=generate_summary(sentences,sentence_scores,average)
    print(summary)
    return summary


# url=input('Enter the URL to summarize')
# getdata(url)
