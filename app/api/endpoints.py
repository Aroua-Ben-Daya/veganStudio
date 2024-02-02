import json
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.entities.recipe import Recipe
from app.schemas.recipe import RecipeAddSchema
from app.utils.encoder import AlchemyEncoder
from app.core.config import Settings

router = APIRouter()

settings = Settings()

@router.get("/recipe")
def get_recipes(db: Session = Depends(get_db)):
    recipes = Recipe.getAll(db)
    result = json.loads(json.dumps(recipes, cls = AlchemyEncoder, skipkeys=True))
    return JSONResponse(content = result, status_code = 200)

@router.post("/recipe")
def add_recipe(recipe: RecipeAddSchema, db: Session = Depends(get_db)):
    new_recipe: Recipe = Recipe(**recipe.dict())
    new_recipe.save(db)
    return JSONResponse(content = {"message": "recipe added","recipe_id": new_recipe.id}, status_code = 201)

@router.delete("/recipe/{id}")
def add_recipe(id: int, db: Session = Depends(get_db)):
    Recipe.deleteOne(id, db)
    return JSONResponse(content = {"message": "recipe deleted","recipe_id": id}, status_code = 201)
