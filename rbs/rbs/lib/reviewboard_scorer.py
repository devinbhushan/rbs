class ReviewBoardScorer(object):
    def __init__(self):
        pass

    def get_data(self):
        raise NotImplementedError("Should have implemented this")

    def score_positive(self):
        raise NotImplementedError("Should have implemented this")

    def score_negative(self):
        raise NotImplementedError("Should have implemented this")