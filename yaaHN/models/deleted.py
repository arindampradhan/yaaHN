# from .. import helpers


class Delete(object):

    """represents a deleted Item for on hackernews"""

    def __init__(self, id, deleted):
        self.id = id
        self.deleted = deleted

    def __repr__(self):
        return "<Delted Item: ID={}>".format(self.id)
