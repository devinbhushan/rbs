from django.db import models
from rbs.lib.reviewboard_scorer import ReviewBoardScorer
from rbs.lib.bugzilla_scorer import BugzillaScorer

class UserStats(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def compute_score(self):
        rb = ReviewBoardScorer(self.name)
        bz = BugzillaScorer(self.name)
        rbp, rbn = rb.evaluate()
        # bz.update_bug_list(rb.get_bug_list())
        # bzp, bzn = bz.evaluate()
        # print bzp, pzn, rbs
        self.score = rbp - rbn
        self.save()
        return self.score

    # def save(self, *args, **kwargs):
    #     super(UserStats, self).save()