import urllib2
import json

def url_to_json(url):
	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	f = opener.open(req)
	return json.loads(f.read())