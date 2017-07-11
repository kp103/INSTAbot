#import all need labraries and functions from files
import os
from wordcloud import WordCloud


def wordcloud():
    #open file in read mode
    open_file=open('wordcloud_content.txt','r')
    #read the text from text file
    text=open_file.read()
    #generate wordcloud of txt from text file
    wordcloud=WordCloud().generate(text)

    raw_input("\t\t\t\t*****************press any key to genrate word cloud*******************")

    #display the generated image
    import matplotlib.pyplot as plt

    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")

    wordcloud=WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.show()
    #this block of code erase all content of txt file and close
    open('wordcloud_content.txt', 'w').close()




