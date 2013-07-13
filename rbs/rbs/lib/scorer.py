class Scorer(object):
    """Abstract class that outlines Scorer functionality, allows for plugins"""

    def __init__(self, username):
        self.username = username
        pass

    def get_data(self):
        """Gets JSON corresponding to user and stores internal
        variables needed for calculations"""
        raise NotImplementedError("Should have implemented this")

    def score_positive(self):
        """Calculates positive score for user"""
        raise NotImplementedError("Should have implemented this")

    def score_negative(self):
        """Calculates negative score for user"""
        raise NotImplementedError("Should have implemented this")
