# from .. import helpers


class User(object):

    """class for User"""

    def __init__(self, id, delay, created, karma, about, submitted):
        self.id = id
        self.delay = delay
        self.created = created
        self.karma = karma
        self.about = about
        self.submitted = submitted

    def __repr__(self):
        return "<Comment: ID={}>".format(self.id)
