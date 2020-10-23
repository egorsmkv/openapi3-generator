import datetime as dt
from marshmallow import Schema, fields

from api.schemas.categories import CategorySchema


class CreatePetBody(Schema):
    name = fields.Str(required=True)


class UpdatePetBody(Schema):
    name = fields.Str()
    categories = fields.List(
        fields.Nested(CategorySchema),
    )


class PetSchema(Schema):
    categories = fields.List(
        fields.Nested(CategorySchema),
        description='Has these categories',
    )

    name = fields.Str()

    created_at = fields.DateTime(
        dump_only=True,
        default=dt.datetime.utcnow,
        title='Created At',
        description='When this item was created'
    )
