from bottle import default_app, response
from bottle import debug
from config import *
import cups

cupsconn = cups.Connection()
app = default_app()
app.catchall = showerrors
