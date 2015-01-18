# from .. import helpers


class Poll(object):

    """represents a Poll for on hackernews"""

    def __init__(self, id, by, kids, score, text, time, title, type):
        self.id = id
        self.by = by
        self.kids = kids
        self.score = score
        self.text = text
        self.time = time
        self.title = title
        self.type = type

    def __repr__(self):
        return "<Comment: ID={}>".format(self.id)
