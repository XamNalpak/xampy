import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk import word_tokenize
from nltk import WordPunctTokenizer
from nltk import download
from nltk import TweetTokenizer
from nltk.corpus import stopwords
import string
from textblob import TextBlob
from textblob.sentiments import PatternAnalyzer
import datetime as datetime
import matplotlib.pyplot as plt
download('stopwords')
download('punkt')
stop_words = set(stopwords.words("english"))

#creates a dataframe from a file path
def makeData(filepath):
    df = pd.read_csv(filepath)
    return df

# prints out quick statistical information
def showInfo(dataframe):
    print(dataframe.describe())
    print("-"*50)
    print(dataframe.info())


def numBarPlot(dataframe, items:list):
    def bar_plot(variable):
        """
            input: variable ex: "Sex"
            output: bar plot & value count
        """
        # get feature
        var = dataframe[variable]
        # count number of categorical variable
        varValue = var.value_counts()
        
        # visualize
        plt.figure(figsize = (9,3))
        plt.bar(varValue.index, varValue)
        plt.xticks(varValue.index, varValue.index.values)
        plt.ylabel("Frequency")
        plt.title(variable)
        plt.show()
        print("{}: \n {}".format(variable, varValue))

    for c in items:
        bar_plot(c)



def catPlots(dataframe,items:list):
    def plot_hist(variable):
        plt.figure(figsize = (9,3))
        plt.hist(dataframe[variable], bins = 50)
        plt.xlabel(variable)
        plt.ylabel("Frequency")
        plt.title("{} distrubution with hist".format(variable))
        plt.show()
    for n in items:
        plot_hist(n)


def countMissing(df):
    print(df.isnull().sum())

def ModeFill(dataframe,colName):
    dataframe[colName] = dataframe[colName].fillna(dataframe[colName].mode()[0])
    return dataframe

def MeanFill(dataframe,colName):
    dataframe[colName] = dataframe[colName].fillna(dataframe[colName].mean().round(3))
    return dataframe


def subSetDf(dataframe,col,value,condition):
    if condition == 'gte':
        df = df[df[col] >= value]
    elif condition == 'lte':
        df = df[df[col] <= value]
    elif condition == 'eq':
        df = df[df[col] == value]
    elif condition == 'gt':
        df = df[df[col] > value]
    elif condition == 'lt':
        df = df[df[col] < value]
    else:
        print(f'{condition} is not a valid selection, choose from the list: \n gt\nlt\gte\nlte\neq')


# takes all things where its not equal to this value        
def OutDF(df,col,val):
    df = df[df[col] != val]
    return df


def renameCols(df,remove,replace):
  df = df.rename(columns=lambda x: x.strip(remove))
  df = df.rename(columns=lambda x: x.replace(' ',replace))
  return df


def dataTypeSplit(df):
    nums = []
    nonnums = []

    for i in df.columns:
      if df[i].dtypes == int or df[i].dtypes == float:
        nums.append(i)
      else:
        nonnums.append(i)

    numdf = df[nums]

    nonnumdf = df[nonnums]

    return numdf,nonnumdf

#sentiment analysis for larger chunks of data, handling punctuation and stop word removal
def Remove_Punctuation(tokenList):
    punctList = list(string.punctuation)
    punctList.remove("'")
    return [word for word in tokenList if word not in punctList]
def Remove_Stop_Words(tokenList, stop_words):
    return [word for word in tokenList if word not in stop_words]
def PreProcess(x):
    return Remove_Punctuation(Remove_Stop_Words(TweetToken(x),stop_words))
def Tokenize(text):
    return TweetTokenizer().tokenize(str(text).lower())


# for seniment analysis on larger chunks of text, bigger than social media
def bigSenti(df,column):
    def Remove_Punctuation(tokenList):
        punctList = list(string.punctuation)
        punctList.remove("'")
        return [word for word in tokenList if word not in punctList]
    def Remove_Stop_Words(tokenList, stop_words):
        return [word for word in tokenList if word not in stop_words]
    def PreProcess(x):
        return Remove_Punctuation(Remove_Stop_Words(TweetToken(x),stop_words))
    def Tokenize(text):
        return TweetTokenizer().tokenize(str(text).lower())
    df = df[df[column].notnull()].copy()
    df[f'{column}_Tokenized'] = df[column].apply(lambda x: PreProcess(x))
    df[f'{column}_Sentiment'] = df[f'{column}_Tokenized'].apply(lambda x: list(TextBlob(" ".join(x), analyzer=PatternAnalyzer()).sentiment))
    
    for sentiment,index in zip(['polarity', 'subjectivity'],[0,1]):
        df[f'{column}_{sentiment}'] = df[f'{column}_Sentiment'].apply(lambda x: x[index])
        
    return df



# takes in a dataframe and a coiumn containing the text from social media sites
def socialSentiment(df,col):
    #load VADER
    analyzer = SentimentIntensityAnalyzer()
    #Add VADER metrics to dataframe
    df['compound'] = [analyzer.polarity_scores(v)['compound'] for v in df[col]]
    df['neg'] = [analyzer.polarity_scores(v)['neg'] for v in data[col]]
    df['neu'] = [analyzer.polarity_scores(v)['neu'] for v in data[col]]
    df['pos'] = [analyzer.polarity_scores(v)['pos'] for v in data[col]]
    df.head(3)
    return df
