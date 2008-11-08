/*
 * The new Helios API, uses cross-frame messaging if needed
 *
 * Ben Adida (ben@adida.net)
 * modified for UCL to be limited to just one election (2008-11-07)
 *
 * 2008-08-25
 */
  
// the API if making calls to the same host as where we currently are.
// this also exposes a cross-frame incoming API

var HELIOS_PREFIX = '';

_Helios_SameSite = Class.extend({
  init: function() {
    // no initialization necessary here
  },
  
  // register event listeners for cross-frame messaging
  setup: function() {
  },
  
  get_election: function(params, callback) {
    $.getJSON(HELIOS_PREFIX + "/election?" + new Date().getTime(), callback);
  },
  
  get_election_voter: function(params, callback) {
    $.getJSON(HELIOS_PREFIX + "/election/voter/" + params['voter_id'] + new Date().getTime(), callback);
  },
  
  get_election_result: function(params, callback) {
    $.getJSON(HELIOS_PREFIX + "/election/result" + new Date().getTime(), callback);
  },
  
  get_election_result_proof: function(params, callback) {
    $.getJSON(HELIOS_PREFIX + "/election/result_proof" +  new Date().getTime(), callback);
  }
});


Helios = new _Helios_SameSite();
