from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Int(
        dump_only=True,
        description='ID',
        example=1,
    )

    name = fields.Str(
        description='Name',
        required=True,
        example='Pug dogs',
    )

    size = fields.Int(
        format='int64',
        description='Number of elements in the category',
        example=20,
    )
