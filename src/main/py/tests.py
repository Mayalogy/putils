import glob
import os

if __name__ == '__main__':
    """
    Runs all unit tests in this package.
    """

    for t in glob.glob("src/main/py/*_test.py"):
        os.system("python " + t)
