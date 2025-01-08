from peewee import SqliteDatabase, Model, AutoField, TextField

import config
from Model.BaseModel import BaseModel


class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Artist'
