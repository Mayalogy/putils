import numpy as np
from putils_stats import StatsUtil
from putils_stats import FrequencyAssessor
from putils_stats import ClassifierFactory
import unittest

class TestClassifierFactory(unittest.TestCase):

    def test_get_classifier_types(self):
        for t in ClassifierFactory().get_classifier_types():
            print t

class TestFrequencyAssessor(unittest.TestCase):

    def test_get_top_terms(self):

        fass = FrequencyAssessor()
        fass.update("dog")
        fass.update("dog")
        fass.update("cat")
        fass.update("pig",33)

        tts= fass.get_top_terms()
        self.assertTrue(tts[0][0]=="pig")
        self.assertTrue(tts[0][1]==33)
        self.assertTrue(tts[1][0]=="dog")
        self.assertTrue(tts[1][1]==2)

        self.assertTrue(len(fass.get_top_terms(2))==2)

class TestStatsUtil(unittest.TestCase):

    def test_by_element_percent_error(self):
        x=np.array([0,1,0,1])
        y=np.array([0,1,0,1])
        self.assertTrue(StatsUtil.by_element_percent_error(x,y)==0)

        y=np.array([1,1,0,1])
        self.assertTrue(StatsUtil.by_element_percent_error(x,y)==.25)

if __name__ == '__main__':
    """
    Needed to run unittests in CLI or PyCharm
    """
    unittest.main()
