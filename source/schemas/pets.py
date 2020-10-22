from marshmallow import Schema, fields
import datetime as dt

from source.schemas.categories import CategorySchema


class PetSchema(Schema):
    categories = fields.List(
        fields.Nested(CategorySchema),
        description='Has these categories',
    )

    name = fields.Str()

    created_at = fields.DateTime(
        dump_only=True,
        default=dt.datetime.utcnow,
        doc_default='When item was created'
    )

    @staticmethod
    def get_name():
        return 'PetSchema'
