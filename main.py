from bottle import get, post, request
from init import app, cupsconn
from os import path, makedirs, extsep
from config import faxdir
from datetime import datetime

@post('/')
def fax():
	for item in request.forms:
		print(item)
		
	pdf = request.files.get('pdf')
	
	# generate filename
	faxfrom = request.forms.get('from')
	faxto = request.forms.get('to')
	faxtime = datetime.now()
	
	filename = path.join(faxdir,
						 str(faxto),
						 str(faxtime.year),
						 str(faxtime.month),
						 str(faxtime.day),
						 str(faxfrom)+extsep+'pdf')
	
	# make path
	makedirs(path.dirname(filename), exist_ok=True)
	pdf.save(filename)
	
	cupsconn.printFile('faxprinter', filename, path.basename(filename))
	return(0)
