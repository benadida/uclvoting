from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

# A client to the Helios site
import heliosclient
import utils

HELIOS_CLIENT = heliosclient.HeliosClient({'consumer_key': 'ucl', 'consumer_secret': 'ucl'},
                        host = '174.129.241.146',
                        port = 80, prefix ='/helios')
                        
ELECTION_ID = '7'

def render_template(template_name, vars = {}):
  t = loader.get_template('ucl/%s.%s' % (template_name, "html"))

  vars_with_utils = vars.copy()
  vars_with_utils['utils'] = utils
  c = Context(vars_with_utils)
  return HttpResponse(t.render(c))

#
# VIEWS
#

def index(request):
  return render_template('index')
  
def vote(request):
  return render_template('vote')
  
def election(request):
  return HttpResponse(utils.to_json(HELIOS_CLIENT.election_get(ELECTION_ID).toJSONDict()))
  
def voter(request):
  pass
  
def submit_vote(request):
  # submit the vote to the Helios Server
  email = request.POST['email']
  encrypted_vote = request.POST['encrypted_vote']
  
  openid = None
  name = "Test User - " + email
  category = None
  
  # submit the vote the Helios server
  HELIOS_CLIENT.open_submit(ELECTION_ID, encrypted_vote, email, openid, name, category)
  return HttpResponse("success");