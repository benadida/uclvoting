from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

# A client to the Helios site
import heliosclient
import utils

HELIOS_CLIENT = heliosclient.HeliosClient({'consumer_key': 'ucl', 'consumer_secret': 'ucl',
                        'access_token': 'ucl', 'access_token_secret' : 'ucl'},
                        host = 'dev.heliosvoting.org',
                        port = 80)
                        
ELECTION_ID = 'ahBkZXYtaGVsaW9zdm90aW5ncg8LEghFbGVjdGlvbhiRAww'

def render_template(template_name, vars = {}):
  t = loader.get_template('ucl/%s.%s' % (template_name, "html"))
  c= Context(vars)
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