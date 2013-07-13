from scorer import Scorer
from util import url_to_json

class BugzillaScorer(Scorer):
    def __init__(self, username):
        self.username = username
        self.bug_list = [i for i in range(2000,2003)]
        self.bug_history = {}
        pass

       #https://api-dev.bugzilla.mozilla.org/latest/bug?product=Bugzilla&priority=P1&status=NEW&creator_name=romaxa
    def _get_data(self):
    	# self.data = url_to_json("https://api-dev.bugzilla.mozilla.org/latest/bug?product=Bugzilla&priority=P1&creator_name%s" % self.username)
    	self.data = {}
    	for bug in self.bug_list:
    		self.bug_history[bug] = url_to_json("https://api-dev.bugzilla.mozilla.org/latest/bug/%s/history" % bug)

    def _score_positive(self):
        return 0

    def _score_negative(self):
    	count = 0
    	# print self.bug_history
    	for bug in self.bug_history:
    		#for each change of state
    		for state in self.bug_history[bug]['history']:
    			#If user is the changer
    			if state['changer']['name'].split('@')[0] == self.username:
    				#chech all changes for status alteration
	    			for change in state.changes:
	    				print change.field_name
    					if change.field_name == "status" and (change.removed == "RESOLVED" or change.removed == "CLOSED"
    							or change.removed == "VERIFIED") and change.added == "REOPENED":
    						count += 1
    	print count
    	return count

    def update_bug_list(self, bug_list):
    	self.bug_list = bug_list

    def evaluate(self):
        """Evaluates score calculations for given user"""
        self._get_data()
        self._score_positive()
        self._score_negative()

b = BugzillaScorer("timeless")
b.evaluate()
