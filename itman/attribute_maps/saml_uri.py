__author__ = 'satyam'

USERNAME = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"
EMAIL = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
FIRSTNAME = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"
LASTNAME = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"

MAP = {
    "identifier": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
    "fro": {
	USERNAME: "username",
        EMAIL: "email",
	FIRSTNAME: "firstname",
	LASTNAME: "lastname"
    },
    "to": {
	'username': USERNAME,
	'email': EMAIL,
	'firstname': FIRSTNAME,
	'lastname': LASTNAME
    }
}