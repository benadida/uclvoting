
# A client to the Helios site
import heliosclient

HELIOS_CLIENT = heliosclient.HeliosClient({'consumer_key': 'ucl', 'consumer_secret': 'ucl'},
                        host = 'localhost',
                        port = 8000)


# get the El Gamal Parameters
params = HELIOS_CLIENT.params()

# generate a keypair
kp = params.generate_keypair()

# create the election remotely
election_id = HELIOS_CLIENT.election_new("UCL Test", kp.pk)

print "election id is: " + election_id

# set open reg
HELIOS_CLIENT.election_set_reg(election_id, open_reg= True)

# set questions
questions = [{"answers": ["ice-cream", "cake"], "max": 1, "question": "ice-cream or cake?", "short_name": "dessert"}]
HELIOS_CLIENT.election_questions_save(election_id, questions)

# freeze it
HELIOS_CLIENT.election_freeze(election_id)
