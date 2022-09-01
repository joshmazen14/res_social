import strawberry
import typing

@strawberry.type
class Recipe:
  title: str
  images: typing.List[str]
  components: typing.List['RecipeComponent']
  tags: typing.List[str]

@strawberry.type
class RecipeComponent:
  type: str
  ingredients: typing.List['Ingredient']
  instructions: typing.List[str]
  appliances: typing.List['Appliance']

@strawberry.type
class Ingredient:
  name: str

@strawberry.type
class Appliance:
  name: str

@strawberry.type
class Query:
  title: str
