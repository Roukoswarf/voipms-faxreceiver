#!/usr/bin/python
if __name__ == '__main__':
	import main
	from bottle import run
	
	run(app=main.app, host='::', port=8080, reloader=True, debug=True)
