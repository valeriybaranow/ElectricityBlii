import config
from peewee import *
from pyrogram import Client

conn = SqliteDatabase(config.DATABASE)


class BaseModel(Model):
    class Meta:
        database = conn


class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Artist'


artist = Artist.get(Artist.artist_id == 1)

print('artist: ', artist.artist_id, artist.name)  # artist:  1 AC/DC

# cursor = conn.cursor()

conn.close()

# app = Client(
#     "valerybaranov"
# )
#
#
# @app.message_handler(commands=['start'])
# def welcome(message):
#     sti = open('static/1.webp', 'rb')
#     app.send_sticker(message.chat.id, sti)
#
#     app.send_message(
#         message.chat.id,
#         "Добро пожаловать {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот оплаты электроэнергии по адресу ул. Херсонская, дом. 10, кв. 8.".format(message.from_user, bot.get_me()),
#         parse_mode='html'
#     )
#
#
# app.run()
