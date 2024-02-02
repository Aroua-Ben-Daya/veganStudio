from pydantic import BaseModel


class RecipeSchema(BaseModel):
    id: int
    name: str
    email: str
    recipe_name: str
    ingredients: str
    methode: str
    region: str

class RecipeAddSchema(BaseModel):
    name: str
    email: str
    recipe_name: str
    ingredients: str
    methode: str
    region: str