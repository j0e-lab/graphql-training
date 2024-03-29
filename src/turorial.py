# 以下サイトのコードをコピペしただけのファイル。
# strawberryで何ができるか端的にコードベースで確認できるようにしたかった。

# (1) 必要なライブラリをインポートする
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


# (2) User型を定義する
@strawberry.type
class User:
    name: str
    age: int


# (3) Query(データの読み込み)を行うクラスを定義する
@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Shota", age=22)
    
@strawberry.type
class Mutation:
    @strawberry.field
    def add_user(self, user: User) -> User:
        return User(name="Adrian Beltre", age=45)


# (4) スキーマを定義する
schema = strawberry.Schema(query=Query)

# (5) GraphQLエンドポイントを作成する
graphql_app = GraphQL(schema)

# (6) FastAPIアプリのインスタンスを作る
app = FastAPI()

# (7) /graphqlでGraphQL APIへアクセスできるようにし、適切なレスポンスを出力
app.add_route("/graphql", graphql_app)
