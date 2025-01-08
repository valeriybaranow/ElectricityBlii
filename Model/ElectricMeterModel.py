from peewee import SqliteDatabase, Model, AutoField, TextField, IntegerField, FixedCharField

import config
from Model.BaseModel import BaseModel


class ElectricMeter(BaseModel):
    electric_meter_id = AutoField(column_name='ElectricMeterId')
    owner = FixedCharField(column_name='Owner', max_length=128)
    payer = FixedCharField(column_name='Payer', max_length=255, null=True)
    number = IntegerField(column_name='Number')
    last_indications = IntegerField(column_name='lastIndications', null=True)

    class Meta:
        table_name = 'ElectricMeter'
