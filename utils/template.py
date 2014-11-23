import jinja2

TEMPLATE_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"),
                              autoescape=True)

def render(template_name, parameters):
    return TEMPLATE_ENV.get_template(template_name).render(parameters)