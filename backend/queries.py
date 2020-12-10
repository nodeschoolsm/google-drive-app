from flask import Blueprint
from flask_graphql import GraphQLView
import graphene
import os

queries_graphql = Blueprint('queries_graphql', __name__)

working_directory = os.getcwd() + "/files"

class get_files(graphene.ObjectType):
    files = graphene.List(graphene.String)

class Query(graphene.ObjectType):
    hello = graphene.String()
    get_files = graphene.Field(get_files, path=graphene.String())
    
    def resolve_hello(self, info):
        return 'World'
    def resolve_get_files(self, info, path):
        print(path)
        response = {
            "files": os.listdir(working_directory + path)
        }
        return response


schema = graphene.Schema(query=Query)

queries_graphql.add_url_rule('/graphql', view_func=GraphQLView.as_view(
     'graphql',
    schema=schema,
    graphiql=True,
))