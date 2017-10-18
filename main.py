from bottle import get, post, request
from init import app, cupsconn
from os import path

@post('/')
def fax():
	for item in request.forms:
		print(item)
	filename = request.forms.get('title')
	fullpath = path.join(faxdir, filename+'.pdf')
	with open(fullpath, 'wb', 0) as f:
		f.write(request.body.read())
	cupsconn.printFile('faxprinter', fullpath, filename)
	return(0)
