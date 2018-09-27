from pyramid.view import view_config

@view_config(
	route_name='home_example',
	renderer='templates/home/home.jinja2'
	)
def myview(request):
    return {}