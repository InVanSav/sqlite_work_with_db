import os

from models.db.database import DATABASE_NAME
from models.db.database import create_db
from files.task import tasks
from files.insert_database import insert

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)

    if not db_is_created:
        create_db()

    # insert()

    tasks(7)
