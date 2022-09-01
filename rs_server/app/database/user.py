import strawberry
from pydantic import BaseModel

class User(BaseModel):
  email: str
  password: str
  id: strawberry.ID
  name: str

@strawberry.experimental.pydantic.type(model=User, all_fields=True)
class UserType:
  pass

@strawberry.type
class Query:
  pass


@strawberry.type
class Mutation:
  @strawberry.mutation
  def create_user(self, username: str, password: str) -> User:
    pass

  @strawberry.mutation
  def login(self, username: str, password: str) -> User:
    pass