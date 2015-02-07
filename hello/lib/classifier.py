from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
import os
import pickle 

class Classifier:
    def __init__(self, test_size=0.25):
        # read the dataset
        data_path = os.path.dirname(os.path.abspath(__file__)) + '/data'
        dataset = load_files(data_path, encoding='utf8', decode_error='ignore')
        self.target_names = dataset.target_names

        # split the data set into training and test data
        self.train, self.test, y_train, self.y_test = train_test_split(dataset.data, dataset.target, test_size=test_size)

        # initialize the classifier pipeline
        self.classifier = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('clf', MultinomialNB()),
        ])
        # train the classifier with training data
        self.classifier.fit(self.train, y_train)


    def evaluate(self):
        """ Evaluate the classifier """
        print np.mean(self.classifier.predict(self.test) == self.y_test)

    def classify(self, emails):
        """ Classify the list of emails and assign the predicted labels (e.g. spam or ham) to each one of them """
        result_dict = {'spam': 1, 'ham': 0}
        return [result_dict[self.target_names[cat]] for msg, cat in zip(emails, self.classifier.predict(emails))]

if __name__ == '__main__':
    clf = Classifier()
    result = clf.classify(['Viagra for free!', 'Appointment for tomorrow about the math class'])
    for res in result:
        print "Message: %s => label: %s" % res
