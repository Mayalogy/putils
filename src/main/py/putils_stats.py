import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA

class FrequencyAssessor(object):

    def __init__(self):
        self.terms = dict()

    def update(self, term, amount=1):
        """
        Updates a new incidence of the term
        @param term: A string term to be counted
        @param amount: the amount to increment for this term
        """
        if(term not in self.terms):
            self.terms[term]=0

        self.terms[term]+=amount

    def get_top_terms(self, max=100):
        """
        @param max: The max number of terms to return
        @return: A list of tuples in descending order
        """

        return sorted(self.terms.iteritems(), key=lambda x:x[1], reverse=True)[:max]


class StatsUtil(object):
    
    @staticmethod
    def pca(X):
        """ 
        Principal Component Analysis
        input: X, matrix with training data stored as flattened arrays in rows
        return: projection matrix (with important dimensions first), variance and mean.
        """
        # get dimensions
        num_data,dim = X.shape
        # center data
        mean_X = X.mean(axis=0)
        X = X - mean_X
        if dim>num_data:
            # PCA - compact trick used
            M = np.dot(X,X.T) # covariance matrix
            e,EV = np.linalg.eigh(M) # eigenvalues and eigenvectors
            tmp = np.dot(X.T,EV).T # this is the compact trick
            V = tmp[::-1] # reverse since last eigenvectors are the ones we want
            S = np.sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
            
            for i in range(V.shape[1]):
                V[:,i] /= S
        else:
            # PCA - SVD used
            U,S,V = np.linalg.svd(X)
            V = V[:num_data] # only makes sense to return the first num_data
            
        # return the projection matrix, the variance and the mean
        return V,S,mean_X

    @staticmethod
    def by_element_percent_error(x,y):
        """
        Returns percent error on an element by element basis for those in np array y vs x. Match must be exact to not
        be counted as an error.

        x=array([0, 1, 0, 1])
        y=array([1, 1, 0, 1])

        will return .25 since the first element in x and y are different.

        @type x Numpy array
        @type y Numpy array
        """
        error=0
        for i in range(len(x)):
            if(x[i]!=y[i]):
                error+=1

        return  error*1.0/len(x)

class ClassifierFactory(object):

    def __init__(self, value=None):
        self.classifier_map = ClassifierFactory._init()

    def get_classifier_types(self):
        return self.classifier_map.keys()

    @staticmethod
    def _init():
        classifier_map = dict()
        classifier_map["NearestNeighbors"]=KNeighborsClassifier(3)
        classifier_map["LinearSVM"]=SVC(kernel="linear", C=0.025)
        classifier_map["RandomForest"]=RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
        classifier_map["AdaBoost"]=AdaBoostClassifier()
        classifier_map["NaiveBayes"]=GaussianNB()
        classifier_map["LDA"]=LDA()
        classifier_map["QDA"]=QDA()
        classifier_map["RBFSVM"]= SVC(gamma=2, C=1)
        classifier_map["DecisionTree"]=DecisionTreeClassifier(max_depth=5)
        return  classifier_map

    def get(self, classifier_type):
        print "initializing " + classifier_type + " classifier"
        return self.classifier_map[classifier_type]
