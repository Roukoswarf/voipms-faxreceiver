from bottle import default_app, response, debug
from config import *
import cups

debug(showerrors)
cupsconn = cups.Connection()
app = default_app()
