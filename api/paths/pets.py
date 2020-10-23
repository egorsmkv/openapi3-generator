from apispec import APISpec

from internal.helpers import param, method, bearer, response_json
from internal.statuses import OK, NOT_FOUND
from api.schemas.errors import ApiErrorSchema
from api.requests.pets import CreatePetRequest, UpdatePetRequest
from api.schemas.pets import PetSchema


def add_paths(spec: APISpec):
    spec.path(
        path='/pet/{id}',
        parameters=[
            param('id', 'Identifier of a Pet')
        ],
        operations=dict(
            get=method(
                tags=['pets'],
                summary='Get a pet',
                responses=[
                    response_json(OK, 'An object a Pet', PetSchema),
                    response_json(NOT_FOUND, 'An object does not exist', ApiErrorSchema),
                ],
                operation_id='getPet',
                security=[
                    bearer(),
                ]
            ),
            post=method(
                tags=['pets'],
                summary='Create a pet',
                request_body=CreatePetRequest,
                responses=[
                    response_json(OK, 'A pet is created', PetSchema),
                ],
                operation_id='postPet',
                security=[
                    bearer(),
                ]
            ),
            patch=method(
                tags=['pets'],
                summary='Update a pet',
                request_body=UpdatePetRequest,
                responses=[
                    response_json(OK, 'Response an object of updated pet', PetSchema),
                ],
                operation_id='patchPet',
                security=[
                    bearer(),
                ]
            ),
        ),
    )
