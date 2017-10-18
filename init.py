from bottle import default_app, response
from config import *
import cups

cupsconn = cups.Connection()
printers = cupsconn.getPrinters()
for printer in printers:
	print(printer, printers[printer]["device-uri"])

app = default_app()
