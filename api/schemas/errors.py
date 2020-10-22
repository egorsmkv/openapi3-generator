from marshmallow import Schema, fields


class ApiErrorSchema(Schema):
    code = fields.Int(
        required=True,
    )

    message = fields.Str(
        required=True,
    )

    @staticmethod
    def get_name():
        return 'ApiErrorSchema'
