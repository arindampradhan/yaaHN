# from .. import helpers


class Comment(object):

    """class for the Comment"""

    def __init__(self, id, by, kids, parent, text, time, type):
        self.id = id
        self.by = by
        self.kids = kids
        self.parent = parent
        self.text = text
        self.time = time
        self.type = type

    def __repr__(self):
        return "<Comment: ID={}>".format(self.id)
