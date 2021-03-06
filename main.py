from bottle import get, post, request
from init import app, cupsconn
from os import path, makedirs, extsep
from config import faxdir, printer
from datetime import datetime
from subprocess import call

@post('/')
def fax():
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
						 '{} {}{}{}'.format(
							 str(faxfrom),
							 faxtime.strftime('%H:%M:%S'),
							 extsep,
							 'pdf'
							 )
						 )
	
	# make path
	makedirs(path.dirname(filename), exist_ok=True)
	
	pdf.save(filename)
	
	call(['/usr/bin/pdfjam', '--outfile', filename, '--paper', 'letterpaper', filename])
	
	cupsconn.printFile(printer, filename, path.basename(filename), {})
	return("ok")
