from api.schemas.pets import CreatePetBody, UpdatePetBody
from internal.helpers import FORMAT_JSON


class CreatePetRequest:
    description = 'JSON object with data to create a new pet'
    required = True
    format = FORMAT_JSON
    name = 'CreatePetRequest'
    schema = CreatePetBody


class UpdatePetRequest:
    description = 'JSON object with data to update a pet'
    required = True
    format = FORMAT_JSON
    name = 'UpdatePetRequest'
    schema = UpdatePetBody
