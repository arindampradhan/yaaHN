    # from .. import helpers


class Item(object):

    """item class for the yaaHN"""
    # loose instant of Item class as it varies often according to story,comment,poll,user
    def __init__(self, id=None, deleted=None, type=None, by=None, time=None, text=None, dead=None, parent=None, kids=None, url=None, score=None, title=None, parts=None):
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
        return "<Item: ID={}>".format(self.id)
