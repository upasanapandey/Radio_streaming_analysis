# Function for Data cleaning and Pos Tagging.
# Author: Upasana Pandey
import nltk
from nltk import pos_tag, word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from string import punctuation
import re
def pos_tagging(file, directory):

'''
Function to perform text cleaning and pos-tagging
'''
nltk.download('punkt')
 nltk.download('averaged_perceptron_tagger')
  # nltk.download('stopwords')
  stopwords1 = list(stopwords.words('english')) + list(punctuation) + ["'s"]
   with open(file, 'r') as fr:
        raw = fr.read()
    raw = re.sub('\w*\d\w*', '', raw)
    token = word_tokenize(raw)
    # Removing stopwords
    tokens_without_sw = [word for word in token if not word in stopwords1]
    filtered_words = [
        word for word in tokens_without_sw if word.lower() not in stopwords1]
    filtered_words1 = [
        word for word in filtered_words if not word.startswith("'")]
    # print(tokens_without_sw)
    # print(filtered_words)
    word_tag = pos_tag(filtered_words1)
    # print(word_tag)
    for x, y in word_tag:
        with open(directory+y+".txt", 'a') as f:
            f.write(x+" ")
        f.close()
    y_tag = [(y) for (x, y) in word_tag if(y != '.' and y != ',')]
    y_tag1 = list(dict.fromkeys(y_tag))
    print(y_tag1)
    os.makedirs(directory+"/histogram/")
    os.makedirs(directory+"/wordcloud/")
    for tag in y_tag1:
        # print(tag)
        histogram(directory+tag+".txt", directory+"/histogram/"+tag+"_hist")
        wordcloud(directory+tag+".txt", directory +
                  "/wordcloud/"+tag+"_wordcloud")
    fr.close()
