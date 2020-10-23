from apispec import APISpec
from apispec.yaml_utils import dict_to_yaml

FORMAT_JSON = 'application/json'
FORMAT_TEXT = 'text/plain'


def response(status: str, value: dict):
    return dict(
        key=status,
        value=value
    )


def response_json(status: str, description: str, schema):
    return dict(
        key=status,
        value=dict(
            description=description,
            content={FORMAT_JSON: dict(schema=schema.__name__)}
        )
    )


def response_text(status: str, description: str):
    return dict(
        key=status,
        value=dict(
            description=description,
            content={FORMAT_TEXT: dict(schema=dict(type='string'))}
        )
    )


def method(responses, tags=None, summary=None, request_body=None, operation_id=None, security=None):
    if not tags:
        tags = []

    data_responses = {}
    for it in responses:
        data_responses[it['key']] = it['value']

    data = dict(
        responses=data_responses,
        tags=tags,
    )

    if request_body:
        ref = {'$ref': f'#/components/requestBodies/{request_body().name}'}
        data['requestBody'] = ref

    if summary:
        data['summary'] = summary

    if operation_id:
        data['operationId'] = operation_id

    if security:
        data['security'] = security

    return data


def add_request_bodies(doc, requests):
    doc_raw = doc.to_dict()
    doc_raw['components']['requestBodies'] = make_requests(requests)

    return dict_to_yaml(doc_raw)


def add_schema(spec: APISpec, schema):
    if isinstance(schema, list):
        for item in schema:
            spec.components.schema(item.__name__, schema=item)
    else:
        spec.components.schema(schema.__name__, schema=schema)


def make_request(request):
    ref_name = f'#/components/schemas/{request.schema.__name__}'

    return dict(
        key=request.name,
        value=dict(
            description=request.description,
            required=request.required,
            content={request.format: dict(schema={'$ref': ref_name})}
        )
    )


def make_requests(lst: list):
    requests = {}

    for item in lst:
        data = make_request(item)
        requests[data['key']] = data['value']

    return requests


def param(name: str, description: str):
    return {'name': name, 'in': 'path', 'required': True, 'description': description, 'schema': {'type': 'string'}}


def security_api_key():
    return {'type': 'apiKey', 'in': 'header', 'name': 'X-API-Key'}


def security_jwt():
    return {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}


def api_key():
    return {'ApiKey': []}


def bearer():
    return {'Bearer': []}
