TITLE = 'Swagger Petstore'
DESCRIPTION = 'Swagger Petstore'
VERSION = '1.0.0'

TERMS_OF_USE = 'http://example.com/terms/'

CONTACT_NAME = 'API Support'
CONTACT_URL = 'http://www.example.com/support'
CONTACT_EMAIL = 'support@example.com'

LICENSE_NAME = 'MIT'
LICENSE_URL = 'https://en.wikipedia.org/wiki/MIT_License'

PRODUCTION_SERVER_URL = 'https://production.example.com/'
PRODUCTION_SERVER_DESC = 'Production Server'

DEVELOPMENT_SERVER_URL = 'https://localhost:8000/'
DEVELOPMENT_SERVER_DESC = 'Development Server'

TAGS = [
    dict(
        name='pets',
        description='Everything about your Pets',
        externalDocs=dict(description='Find out more', url='http://swagger.io')
    ),
    dict(
        name='default',
        description='Basic APIs'
    )
]
