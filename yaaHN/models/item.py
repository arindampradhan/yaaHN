    # from .. import helpers


class Item(object):

    """item class for the yaaHN"""

    def __init__(self, id, deleted, type, by, time, text, dead, parent, kids, url, score, title, parts):
        self.id = id
        self.deleted = deleted
        self.type = type
        self.by = by
        self.time = time
        self.text = text
        self.dead = dead
        self.parent = parent
        self.kids = kids
        self.url = url
        self.score = score
        self.title = title
        self.parts = parts

    def __repr__(self):
        return "<Comment: ID={}>".format(self.id)
