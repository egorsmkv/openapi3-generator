from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from schemas import *
from helpers import *

spec = APISpec(
    title='Swagger Petstore',
    version='1.0.0',
    openapi_version='3.0.2',
    info=dict(
        description='A minimal petstore API',
        termsOfService='http://example.com/terms/',
        contact=dict(
            name='API Support',
            url='http://www.example.com/support',
            email='support@example.com'
        )
    ),
    servers=[
        dict(url='https://staging.example.com/v1', description='Staging server')
    ],
    plugins=[MarshmallowPlugin()],
)

api_key_scheme = {'type': 'apiKey', 'in': 'header', 'name': 'X-API-Key'}
jwt_scheme = {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}
spec.components.security_scheme('ApiKey', api_key_scheme)
spec.components.security_scheme('Bearer', jwt_scheme)

spec.components.schema('CategorySchema', schema=CategorySchema)
spec.components.schema('PetSchema', schema=PetSchema)

spec.path(
    path='/category/{id}',
    parameters=[
        path_parameter('id', 'ID of a Category')
    ],
    operations=dict(
        get=request(CategorySchema)
    ),
)

spec.path(
    path='/pet/{id}',
    parameters=[
        path_parameter('id', 'ID of a Pet')
    ],
    summary='Gets a Pet by its ID',
    operations=dict(
        get=request(PetSchema, description='Get a Pet', security=[{'ApiKey': []}]),
        post=request(PetSchema, description='Add a new Pet', security=[{'Bearer': []}])
    ),
)

api_spec = spec.to_yaml()

print(api_spec)
