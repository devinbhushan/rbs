from scorer import Scorer
from rbs.lib.util import url_to_json

class BugzillaScorer(Scorer):
    def __init__(self, username):
        self.username = username
        pass

    def _get_data(self):
    	data = url_to_json("http://localhost:8080/api/search/?q=%s" % self.username)

        raise NotImplementedError("Should have implemented this")

    def _score_positive(self):
        raise NotImplementedError("Should have implemented this")

    def _score_negative(self):
        raise NotImplementedError("Should have implemented this")