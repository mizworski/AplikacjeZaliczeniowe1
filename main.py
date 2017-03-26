from jinja2 import Environment, PackageLoader
from jinja2 import select_autoescape

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template("test.html")

with open("output.html", "w") as out:
    out.write(template.render(
        number=42,
        string="michal",
        collection=list(range(1, 51))
    ))
