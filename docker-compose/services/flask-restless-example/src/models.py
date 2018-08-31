from core import db


class EndpointMixin(object):
    @classmethod
    def prefix(cls):
        return "/api"

    @classmethod
    def resource_name(cls):
        raise NotImplementedError()

    @classmethod
    def create_api(cls, manager):
        raise NotImplementedError()

    @classmethod
    def list_url(cls):
        return "{prefix}/{resource_name}".format(prefix=cls.prefix(), resource_name=cls.resource_name())

    @classmethod
    def details_url(cls, pk):
        return "{prefix}/{resource_name}/{pk}".format(prefix=cls.prefix(), resource_name=cls.resource_name(), pk=pk)


class Collection(db.Model, EndpointMixin):
    __tablename__ = "collections"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, index=True)

    @classmethod
    def prefix(cls):
        return "/v1"

    @classmethod
    def resource_name(cls):
        return cls.__tablename__

    @classmethod
    def create_api(cls, manager):
        return manager.create_api(cls, methods=['GET', 'POST', 'DELETE'], url_prefix=cls.prefix())


class Document(db.Model, EndpointMixin):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document = db.Column(db.Text, nullable=False)

    @classmethod
    def prefix(cls):
        return "/v1"

    @classmethod
    def resource_name(cls):
        return cls.__tablename__

    @classmethod
    def create_api(cls, manager):
        return manager.create_api(cls, methods=['GET'], url_prefix=cls.prefix())


#
# # Create your Flask-SQLALchemy models as usual but with the following two
# # (reasonable) restrictions:
# #   1. They must have a primary key column of type sqlalchemy.Integer or
# #      type sqlalchemy.Unicode.
# #   2. They must have an __init__ method which accepts keyword arguments for
# #      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
# #      supplies such a method, so you don't need to declare a new one).
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode, unique=True)
#     birth_date = db.Column(db.Date)
#
#
# class Computer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode, unique=True)
#     vendor = db.Column(db.Unicode)
#     purchase_time = db.Column(db.DateTime)
#     owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#     owner = db.relationship('Person', backref=db.backref('computers',
#                                                          lazy='dynamic'))
#
#
