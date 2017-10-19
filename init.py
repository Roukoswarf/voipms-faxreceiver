from bottle import default_app, response, debug
from config import *
import cups

debug(True)
cupsconn = cups.Connection()
app = default_app()
