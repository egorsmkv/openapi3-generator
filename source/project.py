from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from config import *
# from .helpers import security_api_key, security_jwt, add_schema
from .helpers import security_jwt, add_schema
from .schemas.categories import CategorySchema
from .schemas.pets import PetSchema

from source.paths import pets, categories

spec = APISpec(
    title=TITLE,
    version=VERSION,
    openapi_version='3.0.2',
    info=dict(
        description=DESCRIPTION,
        termsOfService=TERMS_OF_USE,
        contact=dict(
            name=CONTACT_NAME,
            url=CONTACT_URL,
            email=CONTACT_EMAIL
        )
    ),
    servers=[
        dict(url=PRODUCTION_SERVER_URL, description=PRODUCTION_SERVER_DESC),
        dict(url=DEVELOPMENT_SERVER_URL, description=DEVELOPMENT_SERVER_DESC),
    ],
    tags=TAGS,
    plugins=[
        MarshmallowPlugin(),
    ],
)

# spec.components.security_scheme('ApiKey', security_api_key())
spec.components.security_scheme('Bearer', security_jwt())

add_schema(spec, CategorySchema)
add_schema(spec, PetSchema)

categories.add_paths(spec)
pets.add_paths(spec)
