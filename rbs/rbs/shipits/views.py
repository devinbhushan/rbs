from rbs.lib.util import url_to_json

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext

def index(request):
	context = {}
	if request.method == "POST":
		user = request.POST['user']
		print "username lookup: ", user
		req = url_to_json("http://10.16.20.100:8080/api/search?username="+user)
		context = {'resp': req}
	else:
		print "get"
	return render_to_response("shipits/search.html", context, context_instance=RequestContext(request))


