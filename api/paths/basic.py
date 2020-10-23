from apispec import APISpec

from internal.helpers import method, response, response_text
from internal.statuses import OK, REQUEST_URI_TOO_LONG, DEFAULT


def add_paths(spec: APISpec):
    spec.path(
        path='/ping',
        operations=dict(
            get=method(
                tags=['default'],
                summary='Ping our API',
                responses=[
                    response_text(OK, 'It must be a PONG'),
                ],
            ),
        ),
    )

    spec.path(
        path='/tests/long-uri',
        operations=dict(
            get=method(
                tags=['default'],
                summary='If the URI is long then throw an error',
                responses=[
                    response(REQUEST_URI_TOO_LONG, dict(description='Request URI too large.')),
                    response_text(DEFAULT, 'Unexpected error'),
                ],
            ),
        ),
    )
