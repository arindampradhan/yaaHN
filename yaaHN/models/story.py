# from .. import helpers


class Story(object):

    """class for story"""

    def __init__(self, id, by, kids, score, time, title, type, url):
        self.id = id
        self.by = by
        self.kids = kids
        self.score = score
        self.time = time
        self.title = title
        self.type = type
        self.url = url

    def __repr__(self):
        return "<Story: ID={}>".format(self.id)
