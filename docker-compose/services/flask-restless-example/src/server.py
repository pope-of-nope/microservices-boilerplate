from core import app, db, flask_restless
from models import Collection, Document

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)


def create_v1_endpoints():
    # Create API endpoints, which will be available at /api/<tablename> by
    # default. Allowed HTTP methods can be specified as well.
    Collection.create_api(manager)
    Document.create_api(manager)
    url_prefix = "/v1"
    # manager.create_api(Collection, methods=['GET', 'POST', 'DELETE'], url_prefix=url_prefix)
    # manager.create_api(Document, methods=['GET'], url_prefix=url_prefix)


create_v1_endpoints()


if __name__ == '__main__':
    # start the flask loop
    app.run(host="127.0.0.1", port=5000)
