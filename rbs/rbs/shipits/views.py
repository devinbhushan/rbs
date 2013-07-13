import urllib2
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext

def index(request):
	context = {}
	if request.method == "POST":
		user = request.POST['user']
		print "username lookup: ", user
		req = urllib2.Request("http://10.16.20.100:8080/api/search?username="+user)
		opener = urllib2.build_opener()
		f = opener.open(req)
		data = json.loads(f.read())
		print data
	else:
		print "get"
	return render_to_response("shipits/search.html", context, context_instance=RequestContext(request))


