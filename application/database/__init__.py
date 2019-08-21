from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from application.database.models import Trucker  # noqa
    db.drop_all()
    db.create_all()
