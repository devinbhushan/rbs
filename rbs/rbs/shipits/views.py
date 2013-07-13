from rbs.lib.util import url_to_json
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext

from rbs.shipits.models import *

def index(request):
	context = {}
	if request.method == "POST":
		user = request.POST['user']
		userstats, created = UserStats.objects.get_or_create(name=user)
		if created or not userstats.score:
			score = userstats.compute_score()
		else:
			score = userstats.data
		req = url_to_json("http://10.16.20.100:8080/api/search?q="+user)
		print score
		context = { 'resp': json.dumps(req), 'score': score }
		return HttpResponse(json.dumps(context), mimetype="application/json")
	else:
		print "get"
	return render_to_response("shipits/search.html", context, context_instance=RequestContext(request))


