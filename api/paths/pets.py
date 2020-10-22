from apispec import APISpec

from internal.helpers import param, method, bearer, response
from api.schemas.pets import PetSchema
from internal.statuses import OK


def add_paths(spec: APISpec):
    spec.path(
        path='/pet/{id}',
        parameters=[
            param('id', 'ID of a Pet')
        ],
        summary='Get or Update a pet by its ID',
        operations=dict(
            get=method(
                tags=['pets'],
                responses=response(OK, 'An object a Pet', PetSchema),
                security=[
                    bearer(),
                ]
            ),
            patch=method(
                tags=['pets'],
                responses=response(OK, 'Response an object of updated pet', PetSchema),
            ),
        ),
    )
