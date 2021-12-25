from os import path
import saml2.saml
from configparser import RawConfigParser

ENABLE_SAML2_LOGIN = True
PASSWORD_EXPIRY_TIME = float('inf')

LOGIN_URL = '/saml2/login/'
LOGOUT_VIEW = 'djangosaml2.views.logout'

# config = RawConfigParser()
# config.read('/etc/env/djangoCashSettings.ini')

BASEDIR = path.dirname(path.abspath(__file__))
APPLICATION_HOST_URL = 'https://swiggtel.swiggy.in:8443/'

SAML_CONFIG = {
  # full path to the xmlsec1 binary programm
  'xmlsec_binary': '/usr/bin/xmlsec1',

  # your entity id, usually your subdomain plus the url to the metadata view /home/ccuser/itman/itman
  'entityid': APPLICATION_HOST_URL,

  # directory with attribute mapping
  'attribute_map_dir': path.join(BASEDIR, 'attribute-maps'),

  # this block states what services we provide
  'service': {
      'sp' : {
          'want_response_signed': False,
          'allow_unsolicited': True,
          'name': 'Ipay Dashboard',
          'name_id_format': saml2.saml.NAMEID_FORMAT_PERSISTENT,
          'endpoints': {
              # url and binding to the assertion consumer service view
              # do not change the binding or service name
              'assertion_consumer_service': [
                  (APPLICATION_HOST_URL + '/saml2/acs',
                   saml2.BINDING_HTTP_POST),
                  ],
              # url and binding to the single logout service view
              # do not change the binding or service name
              'single_logout_service': [
                  (APPLICATION_HOST_URL + '/saml2/ls/',
                   saml2.BINDING_HTTP_REDIRECT),
                  (APPLICATION_HOST_URL + '/saml2/ls/post',
                   saml2.BINDING_HTTP_POST),
                  ],
              },

           # attributes that this project need to identify a user
          'required_attributes': ['username'],
          'allow_unknown_attributes': False,
           # attributes that may be useful to have but not required
          'optional_attributes': ['email', 'firstname', 'lastname'],
          },
      },

  # where the remote metadata is stored
  'metadata': {
      'local': ['/etc/env/Swiggtel.xml'],
      },

  # set to 1 to output debugging information
  'debug': 1,

  # Signing
  # 'key_file': path.join(BASEDIR, 'mycert.key'),  # private part
  # 'cert_file': path.join(BASEDIR, 'mycert.pem'),  # public part

  # Encryption
  # 'encryption_keypairs': [{
  #     'key_file': path.join(BASEDIR, 'mycert.key'),  # private part
  #     'cert_file': path.join(BASEDIR, 'mycert.pem'),  # public part
  # }],

  }

ACS_DEFAULT_REDIRECT_URL = '/admin/'
SAML_CREATE_UNKNOWN_USER = True

SAML_ATTRIBUTE_MAPPING = {
    'username': ('username', ),
    'email': ('email', ),
    'firstname': ('first_name',),
    'lastname': ('last_name', )
}