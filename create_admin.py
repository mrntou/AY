from AY.models import *
from AY import db
admin = Admin(username='admin', password='admin')
db.session.add(admin)
db.session.commit()
print('Done!')