import numpy as np
import pylab as pl
from scipy.cluster.vq import kmeans2
from scipy.cluster.vq import vq

class KMeansClusterer(object):
            
    @staticmethod
    def cluster(points, num_clusters):
        """
        Clusters a number of points into the specified number of clusters.
        
        @param points: A list of n dimensional points to be classified.
        @param num_clusters: The number of desired classes.
        @return classes_w_points, centroids: A list where each entry is a list of Point objects representing a class. Word
        centroids.
        """

        print "generating feature matrix from points into %d classes" % num_clusters
        features = PayloadPoint.get_features(points)
        print "starting kmeans on features of shape: "
        print features.shape    
        centroids,variance=kmeans2(features,num_clusters)
        print "assigning observation class codes"
        code,distance=vq(features,centroids)

        num_clusters_w_points=[[]]*num_clusters
        for i in range(num_clusters):
            ndx = pl.where(code==i)[0]
            classes_w_points[i]=[]

            for j in range(len(ndx)):
                points[ndx[j]].labels.append(i) #add class label to the point                    
                classes_w_points[i].append(points[ndx[j]])    #add the point to the class list

        return classes_w_points, centroids
    
class PayloadPoint(object):
    """
    Represents an N dimensional point with associated metadata.
    
    @param features: numpy array of normalized feature values
    @type meta_data: dict of key value pairs representing any associated metadata, i.e. source,"http://blah.com/blah1"
    """
    
    def __init__(self, features, meta_data):
        self.features=features
        self.meta_data=meta_data
        
        self.labels=[]
        """ Any labels assigned to the point """
        
    @staticmethod
    def construct_from_source(features, source):
            return PayloadPoint.construct_from_metadata_tuples(features, [("source", source)])

    @staticmethod
    def construct_from_metadata_tuples(features, metadata_name_value_tuples):
        """
        list of metadata name and metadata value tuples. Example: ("keypoint", 33)
        """

        metadata=dict()
        for t in metadata_name_value_tuples:
            metadata[t[0]]=t[1]

        return PayloadPoint(features,metadata)

    @staticmethod
    def get_features(points):
        """
        @param points: A list of PayloadPoint objects.
        @return: A numpy array where each row represents a given point's feature vector.
        """
            
        f_list = []
        for i in range(len(points)):
            f_list.append(points[i].features)
            
        return np.vstack(f_list)
        
    def get_source(self):
        return self.meta_data["source"]
        
    @staticmethod
    def get_sources(points):
        """
        Returns source values for a list of Point objects from each point's metadata.
        """
            
        s_list = []
        for i in range(len(points)):
            s_list.append(points[i].get_source())
            
        return np.vstack(s_list)