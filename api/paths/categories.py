from apispec import APISpec

from internal.statuses import OK
from internal.helpers import param, method, response_json
from api.schemas.categories import CategorySchema


def add_paths(spec: APISpec):
    spec.path(
        path='/category/{id}',
        parameters=[
            param('id', 'Identifier of a category')
        ],
        operations=dict(
            get=method(
                tags=['categories'],
                responses=[
                    response_json(OK, 'Information about a category', CategorySchema),
                ]
            )
        ),
    )
