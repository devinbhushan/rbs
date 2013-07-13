from scorer import Scorer
from util import url_to_json
from math import log


class ReviewBoardScorer(Scorer):
    """Implements Scorer class with ReviewBoard specific scoring heuristics"""

    def __init__(self, username, grace_period, review_length):
        self.username = username
        self.grace_period = int(grace_period)
        self.review_length = int(review_length)
        self.shipits_recv = []
        self.shipits_given = []
        self.response_results = {}
        pass

    def _get_data(self):
        """Gets data from ReviewBoard REST API and gets code that user shipit'ed
        as well as code he submitted for review"""
        json_data = url_to_json("http://localhost:8080/api/search/?q=%s" % self.username)

        for review in json_data["search"]["reviews"]:
            if review["ship_it"] is True:
                self.shipits_given.append(review)

        for shipit_received in json_data["search"]["shipits_received"]:
            self.shipits_recv.append(shipit_received)

        self.response_results = json_data["search"]["response_results"]

    def _score_positive(self):
        """Calculates positive component of the user's score based on
        number of shipits received and number given"""
        num_given = len(self.shipits_given)
        num_received = len(self.shipits_recv)
        return (num_given * 10) + (num_received * 5)

    def _score_negative(self):
        """Calculates negative component of the user's score based on
        time taken to reply to tagged review requests and time taken
        to ship code from a review request from the time it was posted"""
        negative_score = 0
        for result in self.response_results.values():
            result = float(result)
            if result < self.grace_period:
                pass
            else:
                result -= self.grace_period
                negative_score += 10*(log(result)/(log(self.review_length)))
        print negative_score
        return negative_score

    def get_bug_list():
        """Return bug list from JSON"""
        return json_data["search"]["bugs_closed"]

    def evaluate(self):
        """Evaluates score calculations for given user"""
        self._get_data()
        return self._score_positive(), self._score_negative(), self.response_results

# rbs = ReviewBoardScorer("emills", 3600, 1209600) # 1 hour and 14 days
# rbs.evaluate()
