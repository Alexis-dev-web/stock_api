import os
from flask.cli import FlaskGroup
from app import app
from sqlalchemy import func

from DBMigration import db

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    if os.getenv('FLASK_ENV', 'development') == 'development':
        try:
            db.drop_all()
        except Exception:
            pass

        db.create_all()
        db.session.commit()
    else:
        print("you shall not pass")

if __name__ == "__main__":
    cli()
