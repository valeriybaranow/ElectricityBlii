from peewee import SqliteDatabase, Model

import config


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(config.DATABASE)  # соединение с базой, из шаблона выше
