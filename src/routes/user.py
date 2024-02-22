import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from src.type.user import Mutation, Query

user = APIRouter()
schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL
user.add_route('/graphql', graphql_app)
