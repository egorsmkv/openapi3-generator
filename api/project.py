from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from internal.helpers import security_jwt, add_schema
from api.schemas.categories import CategorySchema
from api.requests.pets import CreatePetRequest, UpdatePetRequest
from api.schemas.pets import PetSchema, CreatePetBody, UpdatePetBody
from config import *

from api.paths import basic, pets, categories

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
        ),
        license=dict(
            name=LICENSE_NAME,
            url=LICENSE_URL,
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

# add schemas
add_schema(spec, CategorySchema)
add_schema(spec, PetSchema)
add_schema(spec, [
    CreatePetBody,
    UpdatePetBody,
])

# add paths
modules = [
    basic,
    categories,
    pets
]
for module in modules:
    module.add_paths(spec)

# list all request classes
requests = [
    CreatePetRequest,
    UpdatePetRequest,
]
