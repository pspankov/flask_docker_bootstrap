from flask import Flask, jsonify
from flask_graphql import GraphQLView
from py2neo import Graph
from flask_restx import Api

from src.schemas import schema


app = Flask(__name__)
app.config.from_object("src.config.Config")


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

api = Api(
    app,
    version="1.0",
    title="TodoMVC API",
    description="A simple TodoMVC API",
)

from .rest_api import *


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "The requested URL was not found on the server."}), 404


@app.route("/")
def hello_world():
    return jsonify(hello="world")
