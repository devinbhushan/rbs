import json
from django.db import models
from rbs.lib.reviewboard_scorer import ReviewBoardScorer
from rbs.lib.bugzilla_scorer import BugzillaScorer

class UserStats(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    score = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def compute_score(self):
        rb = ReviewBoardScorer(self.name, 3600, 1209600)
        bz = BugzillaScorer(self.name)
        rbp, rbn, times = rb.evaluate()
        # bz.update_bug_list(rb.get_bug_list())
        # bzp, bzn = bz.evaluate()
        # print bzp, pzn, rbs
        self.score = rbp - rbn
        self.data = json.dumps({'rbp':rbp, 'rbn':rbn, 'times': times})
        self.save()
        return self.data


    # def save(self, *args, **kwargs):
    #     super(UserStats, self).save()