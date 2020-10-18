from marshmallow import Schema, fields
import datetime as dt


class CategorySchema(Schema):
    id = fields.Int(dump_only=True, description='ID')
    name = fields.Str(description='A name', required=True)
    size = fields.Int(format='int64', description='Size of name')


class PetSchema(Schema):
    categories = fields.List(fields.Nested(CategorySchema), description='Has these categories')
    name = fields.Str()
    created_at = fields.DateTime(
        dump_only=True, default=dt.datetime.utcnow, doc_default='When item was created'
    )
