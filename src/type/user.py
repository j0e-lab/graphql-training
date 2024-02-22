import typing

import strawberry

from ..config.database import connection
from ..models.user import users


@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str


@strawberry.type
class Query:
    @strawberry.field
    # TODO Queryでcrud処理をしたらどうなるか
    def user(self, info, id: int) -> User:
        return connection.execute(users.select().where(users.c.id == id)).fetchone()

    def users(self, info) -> typing.List[User]:
        return connection.execute(users.select()).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> User:
        connection.execute(
            users.insert().values(name=name, email=email, password=password)
        )
        return connection.execute(
            users.select().where(users.c.email == email)
        ).fetchone()

    @strawberry.mutation
    def update_user(self, info, name: str, email: str, password: str) -> User:
        connection.execute(
            users.update()
            .where(users.c.id == id)
            .values(name=name, email=email, password=password)
        )
        return connection.execute(users.select().where(users.c.id == id)).fetchone()

    # TODO 例外処理つける
    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        connection.execute(users.delete().where(users.c.id == id))
        return True
