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
    openapi_version=OPENAPI_VERSION,
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
    servers=SERVERS,
    tags=TAGS,
    externalDocs=dict(url=EXTERNAL_DOCS_URL, description=EXTERNAL_DOCS_DESCRIPTION),
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
