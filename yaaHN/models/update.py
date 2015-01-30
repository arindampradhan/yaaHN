# from .. import helpers


class Update(object):

    """class for the Update"""

    def __init__(self, items, profiles):
        self.items = items
        self.profiles = profiles

    def __repr__(self):
        return "items updated : {0}".format(len(items))
