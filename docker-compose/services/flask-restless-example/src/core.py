import flask
import flask_sqlalchemy
import flask_restless

# examples of Flask Restless:
# https://github.com/jfinkels/flask-restless/blob/master/examples/server_configurations/separate_endpoints.py

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///document-server.sqlite3'
db = flask_sqlalchemy.SQLAlchemy(app)
