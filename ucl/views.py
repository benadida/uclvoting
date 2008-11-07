from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

def render_template(template_name, vars = {}):
  t = loader.get_template('ucl/%s.%s' % (template_name, "html"))
  c= Context(vars)
  return HttpResponse(t.render(c))

# Create your views here.
def index(self):
  return render_template('index')