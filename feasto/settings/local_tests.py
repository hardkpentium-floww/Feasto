import uuid

from feasto.settings.local import *
from feasto.settings.base_pg_db import *

DATABASES['default']['TEST'].update({
    'NAME':  str(uuid.uuid4()),
    'ENGINE': os.environ.get('RDS_DB_ENGINE'),
    'CHARSET': 'UTF8'
})

