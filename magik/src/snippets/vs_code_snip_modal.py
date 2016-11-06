import json


class VSCodeSnip:
    """
    >>> print VSCodeSnip(u"ae\\tan_element()", u"an_element()$0")
    {"an_element()": {"body": ["an_element()$0"], "prefix": "ae", "description": "an_element()"}}
    >>> print VSCodeSnip(u"ae\\tan_element()", u"an_element()$0", u"an element", u"an element description")
    {"an element": {"body": ["an_element()$0"], "prefix": "ae", "description": "an element description"}}
    """
    name = ""
    prefix = ""
    body = []
    desc = ""

    def __init__(self, pref, body, name=None, desc=None):
        """
            init a vs code snippet with values
        Args:
            name (unicode): name of the snippet. if skipped then use the prefix
            pref (unicode): prefix of the snippet. this will trigger the snippet
            body (unicode, list): if string is sent will be split by '\n'
            desc (unicode): description of the snippet. if skipped then prefix or name will be used
        """
        if pref.find("\t") != -1:
            (self.prefix, self.name) = pref.split("\t", 1)
        else:
            self.prefix = pref

        self.body = body if (type(body) == list) else body.split("\n")

        self.name = name or self.name or pref

        self.desc = desc or self.name or pref

    def __repr__(self):
        return json.dumps({self.name: self.to_dict()})

    def to_dict(self):
        dic = {}
        if self.prefix: dic["prefix"] = self.prefix
        if self.body: dic["body"] = self.body
        if self.desc: dic["description"] = self.desc
        return dic
