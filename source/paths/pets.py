from apispec import APISpec

from source.helpers import path, method, bearer, response
from source.schemas.pets import PetSchema
from source.statuses import OK


def add_paths(spec: APISpec):
    spec.path(
        path='/pet/{id}',
        parameters=[
            path('id', 'ID of a Pet')
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
