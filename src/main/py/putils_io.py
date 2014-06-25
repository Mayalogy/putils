import pickle
import os
import yaml
import codecs
import shutil
import urllib2
import posixpath

class Yamlator(object):

    @staticmethod
    def dump(file_path, object_to_dump):
        """
        Dumps object into file and overwrites any pre-existing file.
        """

        if(os.path.exists(file_path)):
            os.remove(file_path)

        f = open(file_path, "w")
        yaml.dump(object_to_dump,f)
        f.close()

    @staticmethod
    def load(file_path):
        s=open(file_path, 'r')
        m=yaml.load(s)
        return m

class SimPickler(object):

    @staticmethod
    def dump(file_path, object_to_dump):
        """
        Dumps object into file and overwrites any pre-existing file.
        """

        if(os.path.exists(file_path)):
            os.remove(file_path)

        output_pkl = open(file_path, 'wb')
        pickle.dump(object_to_dump,output_pkl)
        output_pkl.close()

    @staticmethod
    def big_dump(file_path, object_to_dump):
        """
        Dumps object into temp file, then moves copy over when done to minimize probs.
        """
        SimPickler.dump(file_path+".new", object_to_dump)
        shutil.move(file_path+".new", file_path)

    @staticmethod
    def load(file_path):
        input_pkl = open(file_path, 'rb')
        picled_object = pickle.load(input_pkl)
        input_pkl.close()
        return picled_object

class FileUtil(object):

    @staticmethod
    def delete_files_starting_with(prefix):
        for file in os.listdir("."):
            if file.startswith(prefix):
                os.remove(file)

    @staticmethod
    def delete_files_ending_with(dir, suffix):
        for file in os.listdir(dir):
            if file.endswith(suffix):
                print "deleting " + file
                os.remove(dir+"/"+file)

    @staticmethod
    def dump_string_to_file(file_path, string_to_write):
        file_output = codecs.open(file_path, 'w', 'utf-8')
        file_output.write(string_to_write)
        file_output.close()

class UrlUtil(object):

    @staticmethod
    def download_to_file(url, out_path=None, prefix=None):
        """
        Downloads a file from an url and stores it to out_path. If out_path does not exist, it creates a local file
        and puts it into the stem of the url, i.e. http://blah.com/bla/1.jpg will be stored in bla/1.jpg
        """
        f = urllib2.urlopen(url)

        if(out_path == None):
            d = UrlUtil.get_url_path(url, include_leaf=False)
            out_path=UrlUtil.get_url_path(url)

            if(prefix != None):
                d=posixpath.join(prefix, d)
                out_path=posixpath.join(prefix, out_path)

            if(not os.path.exists(d)):
                os.makedirs(d)

        output = open(out_path,'wb')
        output.write(f.read())
        output.close()

    @staticmethod
    def get_url_path(url, include_leaf=True):
        """
        Returns path of an url, i.e. minus the host and domain name.
        """
        nodes = url.split("/")[3:]
        rpath = []
        s = len(nodes)
        if(not include_leaf):
            s=s-1

        is_first=True
        for i in range(s):
            if(not is_first):
                rpath.append("/")

            rpath.append(nodes[i])
            is_first=False

        return ''.join(rpath)