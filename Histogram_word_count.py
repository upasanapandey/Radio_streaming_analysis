# Function to create Histogram based on wordcount.
# Author : Upasana Pandey

from collections import Counter


def histogram(file, directory):
    '''
    Function to built histogram based on word count
    '''
    counts = word_count(file)
    labels, values = zip(*counts.items())
    print(counts)
    plt.bar(labels, values)

    plt.xlabel('word', fontsize=20)
    plt.ylabel('count', fontsize=20)
    plt.xticks(rotation=45, horizontalalignment='right',
               fontweight='light', fontsize='medium')
    plt.savefig(directory+".png", bbox_inches='tight')
    plt.show()


# Function for word count in each Pos file.
# Upasana Pandey | upasana.p@mastechinfotrellis.com


def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
    f.close()
