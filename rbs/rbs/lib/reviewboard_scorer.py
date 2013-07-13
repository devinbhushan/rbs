from scorer import Scorer
from util import url_to_json


class ReviewBoardScorer(Scorer):
    """Implements Scorer class with ReviewBoard specific scoring heuristics"""

    def __init__(self, username):
        self.username = username
        pass

    def _get_data(self):
        """Gets data from ReviewBoard REST API and gets code that user shipit'ed
        as well as code he submitted for review"""
        json_data = url_to_json("http://localhost:8080/api/search/?q=%s" % self.username)
        self.review_requests = json_data['search']['review_requests']

        for review in json_data["search"]["reviews"]:
            if review["ship_it"] is True:
                print "FOUND TRUE!"

    def _score_positive(self):
        raise NotImplementedError("Should have implemented this")

    def _score_negative(self):
        raise NotImplementedError("Should have implemented this")

    def evaluate(self):
        """Evaluates score calculations for given user"""
        self._get_data()
        self._score_positive()
        self._score_negative()

rbs = ReviewBoardScorer("emills")
rbs.evaluate()
