from bottle import get, post, request
from init import app

@post('/')
def fax():
	postdata = request.body.read()
	print(postdata)
	return(0)