# Function to create word cloud.
# Author : Upasana Pandey

from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def wordcloud(file, directory):
  '''
  Function to build word clouds
  '''
    file_content = open(file).read()
    stopwords1 = set(stopwords.words('english'))
    wordcloud = WordCloud(background_color="white",
                          stopwords=stopwords1).generate(file_content)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    wordcloud.to_file(directory+".png")
