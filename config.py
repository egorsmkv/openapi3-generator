TITLE = 'Simple API'
DESCRIPTION = 'This is a simple project that demonstrates the OpenAPI 3 Generator project'
VERSION = '1.0.0'

TERMS_OF_USE = 'http://example.com/terms/'

CONTACT_NAME = 'API Support'
CONTACT_URL = 'http://example.com/support'
CONTACT_EMAIL = 'support@example.com'

EXTERNAL_DOCS_DESCRIPTION = 'More docs about this API'
EXTERNAL_DOCS_URL = 'http://docs.example.com'

LICENSE_NAME = 'MIT'
LICENSE_URL = 'https://en.wikipedia.org/wiki/MIT_License'

OPENAPI_VERSION = '3.0.3'

SERVERS = [
    dict(url='https://production.example.com', description='Production server'),
    dict(
        url='https://{customer}.stage.example.com:{port}',
        description='Stage server for a customer',
        variables=dict(
            username=dict(
                default='mark',
                description='A customer identifier',
            ),
            port=dict(
                default='8001',
                enum=['8001', '443'],
                description='A customer identifier',
            ),
        )
    ),
    dict(url='http://localhost:8000', description='Development server'),
]

TAGS = [
    dict(
        name='pets',
        description='Everything about your Pets',
        externalDocs=dict(description='Find out more', url='http://swagger.io')
    ),
    dict(
        name='categories',
        description='Everything about categories',
    ),
    dict(
        name='default',
        description='Basic paths'
    )
]
