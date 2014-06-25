from putils_io import Yamlator
from putils_io import UrlUtil

import unittest
import os
import shutil

class TestYamlator(unittest.TestCase):

    def test_dump(self):
        import os
        p="junk88.txt"
        self.assertTrue(not os.path.exists(p))
        Yamlator.dump(p, {'name': "The Cloak 'Colluin'"})
        self.assertTrue(os.path.exists(p))
        os.remove(p)
        self.assertTrue(not os.path.exists(p))

class TestUrlUtil(unittest.TestCase):

    def test_download_to_file(self):
        #test w/ out_path
        UrlUtil.download_to_file("http://github.com/Mayalogy/putils/blob/master/README.md", out_path="123.jpg")
        self.assertTrue(os.path.exists("123.jpg"))
        os.remove("123.jpg")
        self.assertTrue(not os.path.exists("123.jpg"))

        # test w/ no prefix
        UrlUtil.download_to_file("http://github.com/Mayalogy/putils/blob/master/README.md")
        self.assertTrue(os.path.exists("Mayalogy/putils/blob/master/README.md"))
        shutil.rmtree("Mayalogy")
        self.assertTrue(not os.path.exists("Mayalogy"))

        #test w/ prefix
        UrlUtil.download_to_file("http://github.com/Mayalogy/putils/blob/master/README.md", prefix="yowza")

        self.assertTrue(os.path.exists("yowza/Mayalogy/putils/blob/master/README.md"))
        shutil.rmtree("yowza")
        self.assertTrue(not os.path.exists("yowza"))

if __name__ == '__main__':
    """
    Needed to run unittests in CLI or PyCharm
    """
    unittest.main()
