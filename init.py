from bottle import default_app, response
from config import *
import cups

cupsconn = cups.Connection()
app = default_app()
