Problem 3: Learning sentiment-specific word representations from tweets

Task: Sentiment Analysis of Tweets
Sentiment classes:
Negative (-1)
Neutral (0)
Positive (1)

File Contents:-
embedding_learning_corpus.txt
Contains millions of records to be used for training the SSWE model
train.tsv: 
Contains 7605 records to be used for training the model
test.tsv: 
Contains 1317 records to be used for testing and tuning the model parameters

Tweet Tokenizer: 
https://github.com/brendano/ark-tweet-nlp/blob/master/src/cmu/arktweetnlp/Twokenize.java

Classifier to use: [only linear kernel allowed]
http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html 

Pre-trained word embeddings (you can try): [Twitter (2B tweets | 27B tokens): 25d 50d 100d 200d]
http://nlp.stanford.edu/projects/glove/
