def request(schema: object, description='', security=None):
    name = schema.__name__
    data = dict(
        responses={'200': {'description': description, 'content': {'application/json': {'schema': name}}}}
    )

    if security:
        data['security'] = security

    return data


def path_parameter(name: str, description: str):
    return {'name': name, 'in': 'path', 'required': True, 'description': description, 'schema': {'type': 'string'}}
