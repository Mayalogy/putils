from putils_clustering import KMeansClusterer
from putils_clustering import PayloadPoint
import unittest
import numpy as np

class TestKMeansClusterer(unittest.TestCase):

    def test_cluster(self):

        #create synthetic PayloadPoints in an obvious cluster space
        points=[]
        points.append(PayloadPoint.construct_from_source(np.array((1.01,1)), "c0"))
        points.append(PayloadPoint.construct_from_source(np.array((.9,1.01)), "c0"))
        points.append(PayloadPoint.construct_from_source(np.array((1.02,.95)), "c0"))
        points.append(PayloadPoint.construct_from_source(np.array((10,10.1)), "c1"))
        points.append(PayloadPoint.construct_from_source(np.array((9.2,10)), "c1"))
        points.append(PayloadPoint.construct_from_source(np.array((10,9.2)), "c1"))
        points.append(PayloadPoint.construct_from_source(np.array((20,20.1)), "c2"))
        points.append(PayloadPoint.construct_from_source(np.array((19.2,20)), "c2"))
        points.append(PayloadPoint.construct_from_source(np.array((20,19.2)), "c2"))

        clusters, centroids = KMeansClusterer.cluster(points,3)
        for i in range(len(clusters)):
            print "\ncluster %d members:\n" % i
            last=None
            for j in range(len(clusters[i])):
                if(last!=None):
                    print "validating last="+last+" is equal to current " + clusters[i][j].get_source()

                last=clusters[i][j].get_source()

if __name__ == '__main__':
    unittest.main()