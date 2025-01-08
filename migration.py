from playhouse.migrate import *

import config
from Model.ElectricMeterModel import ElectricMeter

# SQLite example:
db = SqliteDatabase(config.DATABASE)

db.connect()
db.create_tables([ElectricMeter])

ElectricMeter.create(owner='Настя', number=1, last_indications=11)
ElectricMeter.create(owner='Валерий', number=1, last_indications=11)
ElectricMeter.create(owner='Валерий', number=1, last_indications=11)
ElectricMeter.create(owner='Ярослав', number=1, last_indications=11)

db.close()

# migrator = SqliteMigrator(db)
#
# title_field = CharField(default='')
# status_field = IntegerField(null=True)
#
# migrate(
#     migrator.add_column('some_table', 'title', title_field),
#     migrator.add_column('some_table', 'status', status_field),
#     migrator.drop_column('some_table', 'old_column'),
# )
