from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Int(
        dump_only=True,
        description='ID',
    )

    name = fields.Str(
        description='A name',
        required=True,
    )

    size = fields.Int(
        format='int64',
        description='Size of name',
    )
