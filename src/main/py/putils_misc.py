import datetime
import glob

class HtmlUtil(object):

    @staticmethod
    def href(link, text):
        """
        Returns a HTML href of the form: <a href="link">text</a>
        @param link: String of link
        @param text: String of text
        @return: the Html
        """

        return "<a href=\""+link+"\">"+text+"</a>"

    @staticmethod
    def anchor(text):
        return "<a name=\""+text+"\">"+text+"</a>"

    @staticmethod
    def ul(string_array):
        """
        Returns HTML ul element w/ each element in the array as li elements.
        """

        if string_array==None:
            return ""

        ul="<ul>\n"
        for s in string_array:
            ul=ul+"<li>" + s + "</li>\n"

        return ul+"</ul>"

    @staticmethod
    def gen_html_entry(title, url, color):
        s=(
        "<td>\n"
            "<table border=\"0\">\n"
                "<tr>\n"
                    "<tr><td>" + title + "</td></tr>\n"
                    "<td bgcolor=\"" + color + "\">\n"
                        "<img src=\"gt/" + url + "\">\n"
                    "</td>\n"
                "</tr>\n"
            "</table>\n"
        "</td>\n\n"
        )
        return s

    @staticmethod
    def date():
        return datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y")

    @staticmethod
    def img(url, caption):
        return "<img src=\"%s\" alt=\"%s\">" % (url, caption)

    @staticmethod
    def title(value):
        return HtmlUtil._basic_tag("title", value)

    @staticmethod
    def td(value):
        return HtmlUtil._basic_tag("td", value)

    @staticmethod
    def tr(value):
        return HtmlUtil._basic_tag("tr", value)

    @staticmethod
    def h1(value):
        return HtmlUtil._basic_tag("h1", value)

    @staticmethod
    def h2(value):
        return HtmlUtil._basic_tag("h2", value)

    @staticmethod
    def _basic_tag(type, value):
        return "<%s>%s</%s>" % (type, value, type)

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        
        raise "name: " + name + " not in Enum set"

class RankedTrie(object):
    """
    Simple Trie w/ ranking based on hash lookup of all returned results.
    """

    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.flag = False
        self.score_map=dict()

    def add(self, char):
        val = self.value + char if self.value else char
        self.children[char] = RankedTrie(val)

    def insert(self, word, score=None):
        node = self
        for char in word:
            if char not in node.children:
                node.add(char)
            node = node.children[char]
        node.flag = True

        if score != None:
            self.score_map[word]=score

    def find(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value

    def all_prefixes(self):
        results = set()
        if self.flag:
            results.add(self.value)
        if not self.children: return results
        return reduce(lambda a, b: a | b,
                     [node.all_prefixes() for
                      node in self.children.values()]) | results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.all_prefixes()

    def autocomplete_with_rank(self, prefix, max=10):
        unscored = self.autocomplete(prefix)
        results_map=dict()
        for s in unscored:
            results_map[s]=self.score_map[s]

        return sorted(results_map.iteritems(), key=lambda x:x[1], reverse=True)[:max]


