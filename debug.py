#!/usr/bin/python
if __name__ == '__main__':
	import main
	from bottle import run, static_file, TEMPLATES
	from os import path

	@main.app.hook('before_request')
	def cacheing_templates_in_dev_mode_is_bad():
		TEMPLATES.clear()

	run(server='cherrypy', app=main.app, host='::', port=8080, reloader=True, debug=True)
