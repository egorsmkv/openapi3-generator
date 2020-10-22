from apispec import APISpec


def response(status: str, description: str, schema):
    name = schema.__name__

    return {status: {'description': description, 'content': {'application/json': {'schema': name}}}}


def method(responses, tags=None, security=None):
    if not tags:
        tags = []

    data = dict(
        responses=responses,
        tags=tags,
    )

    if security:
        data['security'] = security

    return data


def add_schema(spec: APISpec, schema):
    if not hasattr(schema, 'get_name'):
        raise Exception('No get_name method in this added schema')

    if isinstance(schema, list):
        for i in schema:
            spec.components.schema(i.get_name(), schema=i)
    else:
        spec.components.schema(schema.get_name(), schema=schema)


def path(name: str, description: str):
    return {'name': name, 'in': 'path', 'required': True, 'description': description, 'schema': {'type': 'string'}}


def security_api_key():
    return {'type': 'apiKey', 'in': 'header', 'name': 'X-API-Key'}


def security_jwt():
    return {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}


def api_key():
    return {'ApiKey': []}


def bearer():
    return {'Bearer': []}
